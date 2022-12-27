# Assignment 3

In this assingment you'll be working with Redis and Event Driven Architecture

## Part 1

Read the input from the file, each message is seperated by an empty line. Read
the lines until you reach an empty line publish the sum to the channel `sum`.
Repeat this until you reach the end of the file.

## Part 2

Subscribe to the channel `sum` and if sum is greate than 30k, publish the sum to
channel `high_sum`.

If sum is less than 30k, publish the sum to channel `low_sum`.

## Part 3

Subscribe to the channel `high_sum`, if current unix timestamp even and current
sum is greater than previous one set redis key `max_sum` to the current sum.

## Part 4

Subscribe to the channel `low_sum`, if current unix timestamp odd and current
sum is lower than previous one set redis key `min_sum` to the current sum.

---

Use the python files provided to help you with the assignment. A Github action
will execute all your python code and check if it works.

You can find examples of how to use redis library in the check_redis.py file.

![](diagram.png)
