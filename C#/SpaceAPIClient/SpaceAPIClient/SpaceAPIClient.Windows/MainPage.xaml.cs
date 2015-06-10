using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Runtime.Serialization.Json;
using System.Threading.Tasks;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.Storage;
using Windows.Storage.Streams;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Media.Imaging;
using Windows.UI.Xaml.Navigation;
using Bing.Maps;
using Newtonsoft.Json;
using SpaceAPIClient.Annotations;
using SpaceAPIClient.Models;
using Location = Bing.Maps.Location;

// The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkId=234238

namespace SpaceAPIClient
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page, INotifyPropertyChanged
    {
        private Response _response;

        public Response Response
        {
            get { return _response; }
            set { _response = value;
                OnPropertyChanged();
            }
        }

        public MainPage()
        {
            this.InitializeComponent();
        }

        private async void GetCurrentStatus()
        {
            using (var client = new HttpClient())
            {
                // New code:
                client.BaseAddress = new Uri("http://space.visionsandviews.net");
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                HttpResponseMessage response = await client.GetAsync("spaceapi/admin");
                if (response.IsSuccessStatusCode)
                {
                    var jsonString = response.Content.ReadAsStringAsync();
                    Response = JsonConvert.DeserializeObject<Response>(jsonString.Result);
                    var location = new Location(Response.location.lat, Response.location.lon);
                    myMap.Center = location;
                    myMap.ZoomLevel = 14;
                    Pushpin brixelPushpin = new Pushpin();
                    MapLayer.SetPosition(brixelPushpin, location);
                    myMap.Children.Add(brixelPushpin);
                    var image = await DownloadImage();
                    AddData(image);
                }
            }
        }

        private async Task<BitmapImage> DownloadImage()
        {
            BitmapImage bitmapImage = new BitmapImage();
            using (var client = new HttpClient())
            {
                HttpResponseMessage response = await client.GetAsync(new Uri(Response.logo));
                byte[] img = await response.Content.ReadAsByteArrayAsync();
                InMemoryRandomAccessStream randomAccessStream = new InMemoryRandomAccessStream();
                DataWriter writer = new DataWriter(randomAccessStream.GetOutputStreamAt(0));
                writer.WriteBytes(img);
                await writer.StoreAsync();
                bitmapImage.SetSource(randomAccessStream);
                
            }
            return bitmapImage;
        }

        private void AddData(BitmapImage image)
        {
            SpaceName.Text = Response.space;
            ImageSource.Source = image;
        }

        private void ToggleOpenClose(object sender, RoutedEventArgs e)
        {
            GetCurrentStatus();
        }

        public event PropertyChangedEventHandler PropertyChanged;

        [NotifyPropertyChangedInvocator]
        private void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            var handler = PropertyChanged;
            if (handler != null) handler(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
