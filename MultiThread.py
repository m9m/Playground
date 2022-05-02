# Code created for a question found here: https://stackoverflow.com/questions/70319060/multithreading-multiprocessing-with-a-for-loop-in-python3/

import threading

class MultiThread:

    def __init__(self, func, list_data, thread_cap=10):
        """
        Parameters
        ----------
            func : function
                Callback function to multi-thread
            threads : int
                Amount of threads available in the pool to iterate across a list
            list_data : list
                List of data to multi-thread across
        """
        self.func = func
        self.thread_cap = thread_cap
        self.thread_pool = []
        self.current_index = -1
        self.total_index = len(list_data) - 1
        self.complete = False
        self.list_data = list_data
    
    def start(self):
        for _ in range(self.thread_cap):
            thread = threading.Thread(target=self._wrapper)
            self.thread_pool += [thread]
            thread.start()

    def _wrapper(self):
        while not self.complete:
            if self.current_index < self.total_index:
                self.current_index += 1
                self.func(self.list_data[self.current_index])
            else:
                self.complete = True

    def wait_on_completion(self):
        for thread in self.thread_pool:
            thread.join()

import requests #, time
_my_dict = {}
base_url = "https://www.google.com/search?q="
s = requests.sessions.session()
def example_callback_func(query):
    global _my_dict
    # code to grab data here
    r = s.get(base_url+query)
    _my_dict[query] = r.text # whatever parsed results
    print(r, query)

    

#start_time = time.time()

_my_list = ["examplequery"+str(n) for n in range(100)]
mt = MultiThread(example_callback_func, _my_list, thread_cap=30)
mt.start()
mt.wait_on_completion()


# output queries to file

#print("Time:{:2f}".format(time.time()-start_time))
