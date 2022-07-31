# Getting a server Session ID and Token

Unfortunately, the server session ID and token are not available in the API. You need to open a browser window and preform an **authenticated task** to get the session ID and token from request headers.

This process is always different on every browser window, but it usually boils down to the following steps:

- Open the network monitor (usually in devtools)
- Go to the Minehut panel, and say, upload a file.
- Look for something by the name in the network monitor of "upload" or "file".
- Look at the headers. You need two.
  - Authorization: <token>
  - X-Session-ID: <sessionid>
- Close the browser window.

This *should* be all you need to make authenticated requests, however, something will probably change in the very near future.