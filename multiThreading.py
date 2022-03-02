import concurrent.futures
import time

start = time.perf_counter()


def do_something(secnods):
    print(f"Sleeping {secnods} second(s)...")
    time.sleep(secnods)
    return f"Done Sleeping...{secnods}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # completed as non-order
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # completed as order
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


# Old way
# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s).")
