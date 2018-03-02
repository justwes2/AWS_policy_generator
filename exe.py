template = open("EC2FullAccess.json", "r").read()

apps_raw = open("appList.txt", "r").readlines()
apps = [app.rstrip() for app in apps_raw]

for app in apps:
    fh = open("EC2FullAccess_{}.json".format(app), "w")
    fh.write(template.format(app))
    fh.close()
