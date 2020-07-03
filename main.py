import csv

rewrites = list()
try:
    with open('redirects.csv') as csvfile:
        # Open the CSV file as a CSV
        readCSV = csv.reader(csvfile, delimiter=',')
        for line in readCSV:
            placeholder = "rewrite ^{}$ {} permanent;"
            # strip any whitespace
            from_url = line[0].strip()
            to_url = line[1].strip()
            # build redirect
            redirect = placeholder.format(from_url, to_url)
            # Add to list
            rewrites.append(redirect)

except OSError:
    print('An error has occurred reading the redirect.csv file')
finally:
    csvfile.close()

try:
    with open('redirects.conf', 'w') as file_handler:
        for redirect in rewrites:
            file_handler.write(redirect + '\n')
except OSError:
    print('An error has occurred creating the redirect.conf file')
finally:
    file_handler.close()
