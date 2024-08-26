import socket
import ssl

class Response:

    def __init__(self, content):
        self.text = content
        self.cookies = Utils.GetCookies(content)
        self.html = Utils.GetHTML(content)
        self.status_code = Utils.GetStatusCode(content)

class Utils:

    def GetCookies(content):
        lines = content.splitlines()
        cookies = []
        in_headers = True
        for line in lines:
            if line == '':
                in_headers = False
            if in_headers and line.startswith("Set-Cookie:"):
                cookie_part = line[len("Set-Cookie:"):].strip()
                cookie_attributes = cookie_part.split(';')
                cookies.append(cookie_attributes[0].strip())
        return "; ".join(cookies)

    def GetHTML(content):
        start_index = content.find("<!DOCTYPE html>")
        if start_index != -1:
            return content[start_index:]
        return ""

    def GetStatusCode(content):
        lines = content.splitlines()[0]
        status_code = lines.split()[1]
        return status_code

    def ParamsToString(params):
        params_string = "?"
        for key,value in params.items():
            params_string += f"{key}={value}&"
        return params_string

    def InitializeSSLsocket(host):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        context = ssl.create_default_context()
        sslsock = context.wrap_socket(s, server_hostname=host)
        return sslsock


class Requests:
    PORT = 443
    USER_AGENT = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    CHUNK = 1024

    @staticmethod
    def get(host, path, headers=None,params=None):
        if headers is None:
            headers = {}
    
        if "User-Agent" not in headers:
            headers["User-Agent"] = Requests.USER_AGENT
    
        if params :
            params_string = Utils.ParamsToString(params)
        else:
            params_string = ""

        sslsock = Utils.InitializeSSLsocket(host)

        try:
            sslsock.connect((host, Requests.PORT))
            request = (
                f"GET {path}{params_string} HTTP/1.1\r\n"
                f"Host: {host}\r\n"
            )
            for key, value in headers.items():
                request += f"{key}: {value}\r\n"
    
            request += "Connection: close\r\n\r\n"
            sslsock.sendall(request.encode('utf-8'))
    
            response = b""
            while True:
                chunk = sslsock.recv(Requests.CHUNK)
                if not chunk:
                    break
                response += chunk

            return Response(response.decode())
    
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response("")
    
        finally:
            sslsock.close()



