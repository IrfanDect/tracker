import os,sys,json,requests
import socket
from rich import print
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.align import Align

#banner
banner = Align.center("""
┌┬┐  ┬─┐  ┌─┐  ┌─┐  ┬┌─  ┌─┐  ┬─┐ 
 │   ├┬┘  ├─┤  │    ├┴┐  ├┤   ├┬┘ 
 ┴   ┴└─  ┴ ┴  └─┘  ┴ ┴  └─┘  ┴└─
        
""")

class Main:
    def __init__(self):
        try:
            os.system('clear')
            print(Panel(banner,border_style='gray23 bold',style='blue bold'))
            self.inp = input("\033[94;1mip/domain :\033[97;1m ")
            self.so = socket.gethostbyname(self.inp)
            self.url = f"https://ipinfo.io/{self.so}"
            self.req = requests.get(self.url)
            self.js = json.loads(self.req.text)
            self.city = self.js['city']
            self.ip = self.js['ip']
            self.region = self.js['region']
            self.hostname = self.js['hostname']
            self.loc = self.js['loc'] 
            self.org = self.js['org']
            self.timezone = self.js['timezone']
            self.country = self.js['country']
        except:
            print("[red bold]Gunakan ip Or hostname bager.[reset]")

    @classmethod
    def Tables(self):
        try:
            ap = Main()
            table = Table(box=box.SQUARE,border_style='gray23 bold')
            table.add_column('info',header_style='white bold',style='blue')
            table.add_column('infl2',header_style='white bold',style='green')
            table.add_row('ip',ap.ip)
            table.add_row('hostname',ap.hostname)
            table.add_row('city',ap.city)
            table.add_row('region',ap.region)
            table.add_row('country',ap.country)
            table.add_row('loc',ap.loc)
            table.add_row('org',ap.org)
            table.add_row('timezone',ap.timezone)
            print(table)
        except:
            sys.exit(1)

Main.Tables()
