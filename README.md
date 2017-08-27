# Smart Toaster

Test case of a feedback loop, where the toaster "learns" how the user likes their toast done.


Every time the toast is finished the user tells the toaster whether the toast was under-done, over-done or just right.

This data, along with the toast time and bread width is saved into the database along along with the users name.

A ML algorithm uses the database to determine the optimal toasting time for the given parameters in order to achieve "just-right" toast.

This means that we have a toaster that learns from user preferences.
