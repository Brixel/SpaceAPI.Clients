namespace SpaceAPIClient.Models
{
    public class Response
    {
        public Spacefed spacefed { get; set; }
        public string space { get; set; }
        public string url { get; set; }
        public Cache cache { get; set; }
        public string[] issue_report_channels { get; set; }
        public Contact contact { get; set; }
        public State state { get; set; }
        public string api { get; set; }
        public Location location { get; set; }
        public string logo { get; set; }
        public string[] projects { get; set; }
    }
}