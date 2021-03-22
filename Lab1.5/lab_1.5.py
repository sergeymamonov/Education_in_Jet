import glob


def get_ip_and_mask(path):
    ip_set = set()
    for file_name in glob.glob(path):
        with open(file_name) as file:
            for current_line in file:
                if "ip address" in current_line:
                    ip_set.add(current_line.replace("ip address", "").strip())
    return ip_set


print(*get_ip_and_mask("C:\Study\python\config_files\*.txt"), sep="\n")
