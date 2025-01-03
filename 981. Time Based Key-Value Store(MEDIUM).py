"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""


#Input: ["TimeMap", "set", "get", "get", "set", "get", "get"] 
#[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
#Output = [null, null, "bar", "bar", null, "bar2", "bar2"]

class TimeMap:

    def __init__(self):
        self.store = {} #Key = string, Value = list of val, timestamp

    def set(self, key, value, timestamp):
        #DefaultDict can be used here to initialize a vlue to a key
        #I'm using dictionary as a hash map, Key will be the key, value, will be a list of values, as explained at the comment at the self.store line.
        if key not in self.store:
            self.store[key] = [] #Creates the key-value pair of a dict, with the value being a list
        self.store[key].append([value, timestamp]) #If key already exists at the set call, appends the value and timestamp to it
    
    def get(self, key, timestamp):
        ans = "" #Default answer in case of errors
        values = self.store.get(key, []) #Gets the key value that is called by the get function, in case it doesn't exist, we need to get the closest value below this one, for this we use binary search:

        #Binary search:
        l, r = 0, len(values)-1
        while l <= r: #makes sure the binary search is valid
            m = (l+r) // 2 #sets up MID
            if values[m][1] <= timestamp: #We need to get the closest value BELOW if the valuee called by the get function does not exist, this serves to get the one below
                ans = values[m][0]
                l = m + 1
            else: #Updates the pointer
                r = m - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)