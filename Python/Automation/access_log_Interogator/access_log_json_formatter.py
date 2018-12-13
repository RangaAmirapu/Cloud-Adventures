# Convert and process apache web log file to json
import argparse
import apache_log_parser
import os

def main():
    #get log file path
    parser=argparse.ArgumentParser()
    parser.add_argument("-f", help = "log file path")
    args=parser.parse_args()

    #using apache_log_parser and regex to specify formats
    line_parser = apache_log_parser.make_parser("%h - - %t \"%r\" %s %b")


# Cleaning the line parsed from apache-log_parser and extracting only required info
    outputFile = open(args.f + ".json","w+")
    outputFile.write("[")
    for line in open(args.f):
        log_line_data = line_parser(line)
        outputFile.write('{' + '"remote_host":' '"' + str(log_line_data['remote_host'])+ '"' 
        + ',"time_received_tz_isoformat":' '"' + str(log_line_data['time_received_tz_isoformat'])+ '"'
        + ',"request_first_line":' '"' + str(log_line_data['request_first_line'])+ '"'
        + ',"request_method":' '"' + str(log_line_data['request_method'])+ '"'
        + ',"request_http_ver":' '"' + str(log_line_data['request_http_ver'])+ '"'
        + ',"status":' '"' + str(log_line_data['status'])+ '"'
        + ',"response_bytes":' '"' + str(log_line_data['response_bytes_clf'])+ '"'
        + '},\n')
    outputFile.close()

    filehandle = open(args.f + ".json", 'rb+')
    filehandle.seek(-3, os.SEEK_END)
    filehandle.truncate()
    filehandle.close()

    outputFile = open(args.f + ".json","a")
    outputFile.write("]")
    outputFile.close()

if __name__ == '__main__':
     main()