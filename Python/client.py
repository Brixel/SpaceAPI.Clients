import http.client;
conn = http.client.HTTPConnection("http://space.visionsandviews.net/spaceapi/admin");
conn.request("GET", "/");
response = conn.getresponse();
print(response.status, response.reason);