# MultiprocessedSleepSort

The idea is simple and yet quite nice: <br>

Sort a sequence of natural numbers by letting each number sleep for as many seconds as it is high and then add it to a list. 

For example: <br>
Sequence: [7, 2, 4] <br>
First number sleeps 7 seconds and then adds to the result list.<br>
Second number sleeps 2 seconds and then adds to the result list. <br>
Third number sleeps 4 seconds and then adds to the result list. <br>
Result: [2,4,7]<br>

Credit: I did not come up with this idea. It seems to have originated from a 4chan board. 

## Implementation in Python using Multiprocessing
I use this little exercise to apply the basics of multiprocessing. It is important here to use pool.apply_async such that the workers don't wait for each other to finish.

``` Python
start_sorting(speed=0.1, to_be_sorted=[7, 3, 65, 2, 98])
```

where speed is the factor by which the sleep time is divided. If the sleep time is too short, the algorithm won't work due to the time it takes to assign the work and the time a worker needs to start the work. 

Result<br>
``` Python
[2, 3, 7, 65, 98]
```
