import concurrent.futures
import os
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # done small process first
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # done process order
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


# old methods
# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
