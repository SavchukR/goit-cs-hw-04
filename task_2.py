import multiprocessing

file_paths = ['text_1.txt', 'text_2.txt', 'text_3.txt', 'text_4.txt', 'text_5.txt']

keywords = ['commodo', 'Bob', 'convllis']

def search_files(files, queue):
    results = []
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            found_keywords = [keyword for keyword in keywords if keyword in content]
            results.append({file_path: found_keywords})
    queue.put(results)

if __name__ == '__main__':
    num_processes = 2

    files_per_process = len(file_paths) // num_processes
    file_chunks = [file_paths[i:i + files_per_process] for i in range(0, len(file_paths), files_per_process)]

    queue = multiprocessing.Queue()

    processes = []
    for chunk in file_chunks:
        process = multiprocessing.Process(target=search_files, args=(chunk, queue))
        processes.append(process)
        
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()

    results = []
    while not queue.empty():
        results.extend(queue.get())

    print(results)
