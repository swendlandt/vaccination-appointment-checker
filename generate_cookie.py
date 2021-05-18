from subprocess import check_output

# Note that you have to specify path to script
p = check_output(["node", "../XVIAkamaiGuide/sensordatagen.js"])

sensor_data = p.decode("utf-8")

print(sensor_data)