import base64
import io

base64_string = "QWxsbWlnaHRGb3JFdmVyISEhCg=="

with io.open("output2.pfx", "wb") as outfile:
    outfile.write(base64.b64decode(base64_string))