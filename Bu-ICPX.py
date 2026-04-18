import requests
from datetime import datetime
import os
import csv
from rich.console import Console

class ICPQuery:
    # 初始化类变量
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    domains = []
    real_domains = []

    # 清理数据
    def clean(self):
        self.domains = []
        self.real_domains = []

    # 目标文件
    def check_file(self):
        if not os.path.exists("targets.txt"):
            with open("targets.txt", "w", encoding="utf-8") as f:
                f.write("baidu.com\n")
            print("\033[31m[!] 目标文件 targets.txt 不存在！已创建。\033[0m")

    # 目标检查
    def check_target(self):
        try:
            with open("targets.txt", "r", encoding="utf-8") as f:
                if f.read().strip() == "":
                    print("\033[31m[!] 目标文件 targets.txt 为空！\033[0m")
                    print("\033[31m[!] 请注意添加查询目标到 targets.txt 文件中！\033[0m")
        except Exception as e:
            print(f"\033[31m[!] 检查目标文件失败: {e}\033[0m")

    # 读取文件
    def read_file(self):
        try:
            with open("targets.txt", "r", encoding="utf-8") as f:
                self.domains = [line.strip() for line in f.readlines() if line.strip()]
        except Exception as e:
            print(f"\033[31m[!] 读取文件 targets.txt 失败: {e}\033[0m")

    # 去重
    def remove_duplicates(self):
        self.real_domains = list(set(self.real_domains))

    # 设置域名
    def set_domain(self):
        for d in self.domains:
            cleaned_domain = d.replace("https://", "").replace("http://", "").replace("www.", "")
            if cleaned_domain:
                self.real_domains.append(cleaned_domain)
    
    # 手动查询
    def manual_query(self):
        domain = input("请输入域名：").strip()
        if not domain:
            print("\033[31m[!] 域名不能为空！\033[0m")
            return False
        
        url = f"https://www.huodaidaohang.cn/commontools/php/apihz.php?action=icp-query&domain={domain}"
        try:
            response = requests.get(url, headers=self.headers, timeout=2.5)
            response.raise_for_status()
            
            if "域名格式不正确" in response.text:
                print(f"\033[31m[!] 域名格式不正确: {domain}\033[0m")
                return False
            elif "查询失败" not in response.text:
                try:
                    data = response.json()
                    print(f"\033[32m[+] {domain} 查询成功！\033[0m")
                    print(f"\033[33m[ICP信息]\033[0m")
                    print(f"类型：{data.get('type', 'N/A')}")
                    print(f"ICP：{data.get('icp', 'N/A')}")
                    print(f"单位：{data.get('unit', 'N/A')}")
                    print(f"域名：{data.get('domain', 'N/A')}")
                    print(f"时间：{data.get('time', 'N/A')}")
                    return True
                except ValueError:
                    print(f"\033[31m[!] 无法解析响应数据: {domain}\033[0m")
                    return False
            else:
                print(f"\033[31m[!] 查询失败！未知错误: {domain}\033[0m")
                return False
        except requests.RequestException as e:
            print(f"\033[31m[!] 网络错误: {e}\033[0m")
            return False
        except Exception as e:
            print(f"\033[31m[!] 未知错误: {e}\033[0m")
            return False

    # 批量查询ICP
    def query(self):
        print("\033[33m[+] 开始批量查询ICP...\033[0m")
        
        if not self.real_domains:
            print("\033[31m[!] 没有有效的域名可查询！\033[0m")
            return
        
        if not os.path.exists("results"):
            os.makedirs("results", exist_ok=True)
        
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        csv_path = os.path.join("results", f"{current_time}.csv")
        
        try:
            with open(csv_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["类型", "ICP", "单位", "域名", "时间"])
                
                for d in self.real_domains:
                    url = f"https://www.huodaidaohang.cn/commontools/php/apihz.php?action=icp-query&domain={d}"
                    try:
                        response = requests.get(url, headers=self.headers, timeout=2.5)
                        response.raise_for_status()
                        
                        if "域名格式不正确" in response.text:
                            print(f"\033[31m[!] 域名格式不正确: {d}\033[0m")
                            continue
                        elif "查询失败" not in response.text:
                            try:
                                data = response.json()
                                print(f"\033[32m[+] {d} 查询成功！\033[0m")
                                print(f"\033[33m[ICP信息]\033[0m")
                                print(f"类型：{data.get('type', 'N/A')}")
                                print(f"ICP：{data.get('icp', 'N/A')}")
                                print(f"单位：{data.get('unit', 'N/A')}")
                                print(f"域名：{data.get('domain', 'N/A')}")
                                print(f"时间：{data.get('time', 'N/A')}")
                                writer.writerow([
                                    data.get('type', 'N/A'),
                                    data.get('icp', 'N/A'),
                                    data.get('unit', 'N/A'),
                                    data.get('domain', 'N/A'),
                                    data.get('time', 'N/A')
                                ])
                            except ValueError:
                                print(f"\033[31m[!] 无法解析响应数据: {d}\033[0m")
                                continue
                        else:
                            print(f"\033[31m[!] 查询失败！未知错误: {d}\033[0m")
                            continue
                    except requests.RequestException as e:
                        print(f"\033[31m[!] 网络错误: {e} - {d}\033[0m")
                        continue
                    except Exception as e:
                        print(f"\033[31m[!] 未知错误: {e} - {d}\033[0m")
                        continue
            
            if os.path.getsize(csv_path) <= 30:
                print("\033[31m[!] 批量查询ICP结束!结果为空！\033[0m")
                os.remove(csv_path)
            else:
                print(f"\033[33m[+] 批量查询ICP结束!结果已保存到 {csv_path}\033[0m")
        except Exception as e:
            print(f"\033[31m[!] 保存结果失败: {e}\033[0m")

console = Console()
text = [
"\n",
"██████╗ ██╗   ██╗      ██╗ ██████╗██████╗ ██╗  ██╗",
"██╔══██╗██║   ██║      ██║██╔════╝██╔══██╗╚██╗██╔╝",
"██████╔╝██║   ██║█████╗██║██║     ██████╔╝ ╚███╔╝",
"██╔══██╗██║   ██║╚════╝██║██║     ██╔═══╝  ██╔██╗",
"██████╔╝╚██████╔╝      ██║╚██████╗██║     ██╔╝ ██╗",
"╚═════╝  ╚═════╝       ╚═╝ ╚═════╝╚═╝     ╚═╝  ╚═╝",
"——————————— Bu-ICPX v1.0.0 - ICP查询工具 ———————————",
"[*] 项目地址:[blue]https://github.com/Bu7terf1y/Bu-ICPX[/blue]",
"[*] By.Bu7terf1y",
"[*] 说明:批量查询ICP信息的目标文件为 targets.txt"
]
# 起始颜色（浅粉）
start = (255, 182, 193)   # light pink
# 结束颜色（深紫）
end = (128, 0, 128)       # purple

lines = len(text)

for i, line in enumerate(text):
    # 线性插值
    r = int(start[0] + (end[0] - start[0]) * i / (lines - 1))
    g = int(start[1] + (end[1] - start[1]) * i / (lines - 1))
    b = int(start[2] + (end[2] - start[2]) * i / (lines - 1))
    console.print(line, style=f"rgb({r},{g},{b})", highlight=False)

icp = ICPQuery()
icp.check_file()
icp.check_target()
while True:
    print("\n=========================================")
    choice = input("请输入1.手动查询 2.批量查询 3.退出：").strip()
    if choice == "1":
        icp.manual_query()
    elif choice == "2":
        icp.clean()
        icp.read_file()
        icp.set_domain()
        icp.remove_duplicates()
        icp.query()
    elif choice == "3":
        print("\033[33m[+] 程序退出！\033[0m")
        break
    else:
        print("\033[31m[!] 输入错误！请输入1、2或3。\033[0m")
