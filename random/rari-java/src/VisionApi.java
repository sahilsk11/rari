import java.net.*;

public class VisionApi {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://example.com");
            try {
                HttpURLConnection con = (HttpURLConnection) url.openConnection();
                con.setRequestMethod("GET");
            } catch (java.io.IOException e) {
                System.out.println("Could not connect");
            }
        } catch (java.net.MalformedURLException e) {
            System.out.println("Invalid URL");
        }
    }
}
