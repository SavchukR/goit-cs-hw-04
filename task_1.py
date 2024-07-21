import threading

# config
num_threads = 2
file_paths = ['text_1.txt', 'text_2.txt', 'text_3.txt', 'text_4.txt', 'text_5.txt']

keywords = ['commodo', 'Bob', 'convllis']

def search_files(files, output, index):
    results = []
    for file_path in files:
        print(f"index {index} file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            found_keywords = [keyword for keyword in keywords if keyword in content]
            results.append({file_path: found_keywords})
    output[index] = results

files_per_thread = len(file_paths) // num_threads
file_chunks = [file_paths[i:i + files_per_thread] for i in range(0, len(file_paths), files_per_thread)]

threads = []
results = [None] * len(file_chunks)

i = 0
for chunk in file_chunks:
    thread = threading.Thread(target=search_files, args=(chunk,results, i))
    threads.append(thread)
    i += 1

for thread in threads:
    thread.start()

# wait
for thread in threads:
    thread.join()

print(results)
