import requests
import threading

def download_file(url, start_byte, end_byte, thread_id):
    headers = {'Range': f'bytes={start_byte}-{end_byte}'}
    response = requests.get(url, headers=headers, stream=True)

    with open(f'part_{thread_id}.tmp', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

def main(url, num_threads):
    response = requests.head(url)
    file_size = int(response.headers['Content-Length'])
    part_size = file_size // num_threads

    threads = []
    for i in range(num_threads):
        start_byte = i * part_size
        end_byte = start_byte + part_size - 1 if i < num_threads - 1 else file_size - 1
        thread = threading.Thread(target=download_file, args=(url, start_byte, end_byte, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with open('downloaded_file.tmp', 'wb') as file:
        for i in range(num_threads):
            with open(f'part_{i}.tmp', 'rb') as part_file:
                file.write(part_file.read())

    print("Download completed!")

if __name__ == '__main__':
    url = 'YOUR_LARGE_FILE_URL'
    num_threads = 4  # Adjust the number of threads as needed
    main(url, num_threads)