import os

import process_packages

location = os.getcwd()
location += "\\tests\\"
tests = []
answers = []
for filename in os.listdir(location):
    f = open(location + filename, 'r')

    if filename[-1] != 'a':
        # Test file
        buffer_size, n_requests = map(int, f.readline().strip().split())
        requests = []
        for i in range(n_requests):
            arrival_time, process_time = map(int, f.readline().strip().split())
            requests.append(process_packages.Request(arrival_time, process_time))
        tests.append((buffer_size, n_requests, requests))

    else:
        # Answer file
        responses = []
        for line in f:
            responses.append(int(line.strip()))
        answers.append(responses)

    f.close()

for i, test in enumerate(tests):

    buffer_size, n_requests, requests = test
    buffer = process_packages.Buffer(buffer_size)
    responses = process_packages.process_requests(requests, buffer)

    output_response = []
    for response in responses:
        output_response.append(response.started_at if not response.was_dropped else -1)

    if output_response != answers[i]:
        print("Test %d failed." % (i + 1))
    else:
        print("Test %d OK." % (i + 1))
