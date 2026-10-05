# Assignment 4: Heap Data Structures

**Student:** Bharath Kumar Origanti  
**Course:** Algorithms and Data Structures  
**Professor:** Michael Solomon, PhD  
**University:** University of the Cumberlands  

## Project Overview

This project demonstrates the implementation and analysis of heap data structures in Python. It includes a Heapsort implementation and a max-heap priority queue that can be used for task scheduling.

## Files

- `heapsort.py` - Implements Heapsort using a max heap.
- `priority_queue.py` - Implements a max-heap priority queue and a simple task scheduler.
- `Assignment_4_Heap_Data_Structures_Report_Final_with_References (2).docx` - Written report containing the design, complexity analysis, algorithm comparison, and references.

## Heapsort

The Heapsort program first builds a max heap from the input list. It then repeatedly moves the largest value to the end of the list and restores the heap property.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

## Priority Queue

The priority queue uses a max heap. Tasks with higher priority values are processed before tasks with lower priority values.

The implementation supports:
- Insert a task
- Extract the highest-priority task
- Increase a task's priority
- Decrease a task's priority
- Check whether the queue is empty

## How to Run

Python 3 is required.

Run the Heapsort program:

python heapsort.py

Run the Priority Queue and scheduler:

python priority_queue.py

## Summary

Heapsort provides predictable O(n log n) performance in the best, average, and worst cases. A heap is also useful for implementing priority queues because insertion and removal of the highest-priority element can be performed efficiently. The priority queue example demonstrates how a max heap can be applied to a basic task-scheduling problem.
