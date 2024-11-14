from http.cookies import SimpleCookie
import time


class TrackingCookies:
    def __init__(self):
        self.cookie = SimpleCookie()
        
    def set_cookie(self, site_name):
        visit_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.cookie[site_name] = visit_time
        self.cookie[site_name]["path"] = "/"
        print(f"{site_name} sayti uchun cookie yaratildi: {self.cookie[site_name].value}")
    
    def show_cookies(self):
        print("\nFoydalanuvchi kirgan saytlar:")
        for key, morsel in self.cookie.items():
            print(f"Sayt: {key}, Oxirgi tashrif: {morsel.value}")


if __name__ == "__main__":
    tracker = TrackingCookies()
    

    tracker.set_cookie("example1.com")
    tracker.set_cookie("example2.com")
    tracker.set_cookie("example3.com")
    

    tracker.show_cookies()
