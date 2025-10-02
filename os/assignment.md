### **Assignment Sheet - 1**

**Course:** B.Tech (CSE)
**Year/Semester:** II/III
**Subject Name & Code:** Operating Systems (BCSC 0004)
**Max. Marks:** 15
**Session:** 2025-2026
**Submission date:** 25.09.25

-----

### **Set-1 (Roll No. 1-15)**

**1.** Many CPU-scheduling algorithms are parameterized. For example, the RR algorithm requires a parameter to indicate the time slice. Multilevel feedback queues require parameters to define the number of queues, the scheduling algorithms for each queue, the criteria used to move processes between queues, and so on. These algorithms are thus really sets of algorithms (for example, the set of RR algorithms for all time slices, and so on). One set of algorithms may include another (for example, the FCFS algorithm is the RR algorithm with an infinite time quantum). What (if any) relation holds between the following pairs of algorithm sets?
a. Priority and SJF
b. Multilevel feedback queues and FCFS
c. Priority and FCFS
d. RR and SJF

**2.** Find the average waiting time (A.W.T) and (A.T.A.T) for executing the following process using Preemptive short-job first.

| Process | Burst time | Arrival time |
| :--- | :--- | :--- |
| P1 | 5 | 2 |
| P2 | 13 | 3 |
| P3 | 8 | 0 |
| P4 | 4 | 5 |
| P5 | 10 | 1 |

**3.** Consider three CPU-intensive processes, which require 10, 20 and 30 time units and arrive at times 0, 2 and 6, respectively. How many context switches are needed if the operating system implements a shortest remaining time first scheduling algorithm? Do not count the context switches at time zero and at the end. [gate 2006]

**4.** You are an IT consultant working with a small business owner who is setting up a computer network for their office. The business owner has specific requirements for the operating system, and your task is to recommend the most suitable classification of operating system based on these requirements.
a) The business owner needs an operating system for their office desktop computers. They want an OS that is user-friendly, supports common office software, and is cost-effective. What classification of operating system would you recommend, and why?
b) The business owner also has a server in the office, and they require an OS that can handle multiple user connections, provide file sharing, and ensure data security. What classification of operating system would you recommend for the server, and why?
c) The business owner plans to integrate a real-time system for monitoring and controlling manufacturing equipment. What classification of operating system would you recommend for this specialized task, and why?

**5.** Three processes A, B and C each execute a loop of 100 iterations. In each iteration of the loop, a process performs a single computation that requires tc CPU milliseconds and then initiates a single I/O operation that lasts for tio milliseconds. It is assumed that the computer where the processes execute has sufficient number of I/O devices and the OS of the computer assigns different I/O devices to each process. Also, the scheduling overhead of the OS is negligible. The processes have the following characteristics:

| Process id | tc | tio |
| :--- | :--- | :--- |
| A | 100 ms | 500 ms |
| B | 350 ms | 500 ms |
| C | 200 ms | 500 ms |

The processes A, B, and C are started at times 0, 5 and 10 milliseconds respectively, in a pure time sharing system (round robin scheduling) that uses a time slice of 50 milliseconds. Calculate the time in milliseconds at which process C would complete its first I/O operation is.

**6.** You are the administrator of a multi-user server. One of the users complains that their commands are not executing as expected. Upon investigation, you find that their processes are stuck in the "Blocked" state due to waiting for a network resource. Explain how processes transition between states and how you would address this issue.

**7.** Imagine a simple round-robin scheduling algorithm with a time quantum of 10 milliseconds. Two processes, X and Y, are competing for CPU time. Process X consistently uses less than 10 milliseconds per quantum, while process Y requires more than 10 milliseconds to complete. How would the CPU scheduler handle this situation, and what might be the user's experience with these processes?

**8.** Imagine you're working with a group of non-technical colleagues who are curious about computers. While discussing operating systems, they ask, "Why do we even need an operating system in our computers?" How would you explain the main purpose and significance of an operating system in a relatable scenario or example?

**9.** Let us consider a method used by set of two concurrent processes P1 and P2 in a uniprocessor system for accessing some shared resource. Two shared Boolean variable S1 and S2 used by process P1 and P2 to synchronize their activities and initial value of S1 and S2 is randomly assigned. Methods are:

**P1**

```
While(S1==S2);
Critical Section
S1=S2
```

**P2**

```
While(S1!=S2);
Critical Section
S1= not S2
```

Is the method ensuring synchronization between the process P1 and P2? Justify.

**10.** In Dining philosopher problem, there are X number of dinners and Y number of chopsticks. What is the minimum number of chopsticks required to ensure that there will be no deadlock?

**11.** Person manages a distributed computing cluster where multiple nodes work together to process a large dataset. Each node runs independent tasks, but occasionally, tasks require coordination to avoid conflicts and optimize resource usage.
a) Discuss the challenges of process synchronization in a distributed computing environment and why it's important.
b) Explain how distributed synchronization techniques, such as distributed locks or message passing, can be employed to manage synchronization challenges in the cluster.

**12.** To designing the control system for a set of traffic lights at a busy intersection. The traffic lights need to operate smoothly, preventing traffic jams and accidents. Describe how semaphores can be utilized to manage the state transitions and timing of the traffic lights to ensure efficient traffic flow and safety.

**13.** The administrator of a computing cluster used for scientific simulations. Multiple research groups use the cluster concurrently, and you need to allocate resources fairly. Explain how you could use semaphores to manage resource allocation and ensure that no group monopolizes the cluster's resources.

**14.** Suppose we are designing a Database Management System (DBMS) that serves multiple clients concurrently. The DBMS allows clients to perform read and write operations on the database. Here's how the Reader-Writer problem applies to this scenario: Readers: Clients who want to query and fetch data from the database. Multiple readers should be able to access the database simultaneously to improve query performance. Writers: Clients who want to modify or update data in the database. When a writer is making changes, it's essential to ensure that no other clients (readers or writers) can access or modify the database until the writer's transaction is complete. The following rules apply to this DBMS:

  * Multiple readers can simultaneously execute read queries on the database, as long as no writer is actively modifying the data.
  * Writers must have exclusive access to the database when performing write operations. During a write operation, no other clients (readers or writers) can access or modify the database.
  * While a writer is making changes to the database, new read queries from readers must be queued and executed after the writer's transaction is complete.

Design a solution using semaphores, mutex locks, or other synchronization mechanisms to manage concurrent access to the database in a manner that ensures data consistency and prevents conflicts between readers and writers. Your solution should also prioritize efficient resource utilization to optimize query performance for readers.

-----

### **Set-2 (Roll No. 16-30)**

**15.** Consider the following table of arrival time and burst time for three processes P1, P2 and P3 and given Time Quantum = 2.

| Process | Burst Time (BT) | Arrival Time (AT) |
| :--- | :--- | :--- |
| P1 | 5 ms | 0 ms |
| P2 | 2 ms | 4 ms |
| P3 | 4 ms | 5 ms |

**16.** If Mr. Abhishek aims to run his five programs, each of which typically takes 15 minutes to complete, but he's constrained to a time window of only 15-16 minutes, which operating system would you recommend for optimizing his task? Please explain your choice.

**17.** Consider a set of 5 processes whose arrival time, CPU time needed and the priority are given below:

| Process number | Arrival time(ms) | CPU time | Priority |
| :--- | :--- | :--- | :--- |
| p1 | 0 | 10 | 5 |
| p2 | 0 | 5 | 2 |
| p3 | 2 | 3 | 1 |
| p4 | 5 | 20 | 4 |
| p5 | 10 | 2 | 3 |

If the CPU scheduling policy is SJF, the average waiting time (without preemption) will be?

**18.** Consider the 3 processes, P1, P2 and P3 shown in the table.

| Process | Arrival time | Time Units Required |
| :--- | :--- | :--- |
| P1 | 0 | 5 |
| P2 | 1 | 7 |
| P3 | 3 | 4 |

The completion order of the 3 processes under the policy round robin scheduling with CPU quantum of 2 time units is.

**19.** Consider the following set of processes, with length of CPU bursts given in Millisecond as follows:

| Process | Burst Time | Arrival Time | Priority |
| :--- | :--- | :--- | :--- |
| P1 | 8 | 0 | 3 |
| P2 | 1 | 1 | 1 |
| P3 | 3 | 2 | 2 |
| P4 | 2 | 3 | 3 |
| P5 | 6 | 4 | 4 |

a. Draw the Gantt Charts for FCFS, SJF, Preemptive priority and RR(Quantum=2)
b. What is the turnaround time of each process for above algorithm?
c. What is the waiting time of each process for each of the above algorithm?
d. Which algorithm results in minimum average waiting time?

**20.** You are part of a team working on a robotics project for an industrial automation task. Your team needs to choose an appropriate operating system for the robot's control unit. The choice of operating system will impact the robot's performance and reliability.
a) Explain the key characteristics and requirements of the robotics project that should influence your choice of operating system classification.
b) Considering the project's requirements, justify whether a real-time operating system, a general-purpose operating system, or a specialized embedded operating system would be most suitable for the robot's control unit. Provide reasons for your choice.
c) Outline the potential advantages and drawbacks of your selected operating system classification in the context of the robotics project.

**21.** You are managing a real-time operating system for an autonomous drone. The drone has to perform various tasks with different deadlines, such as navigation and obstacle avoidance. How would you choose a scheduling algorithm to ensure that critical tasks meet their deadlines while maximizing CPU utilization?

**22.** In a computer lab at a university, students are using shared workstations for various tasks, including coding, word processing, and browsing. Describe how a fair-share scheduling algorithm could be employed to ensure that all students have a fair opportunity to use the CPU resources, regardless of their specific tasks.

**23.** A shared variable x, initialized to zero, is operated on by four concurrent processes W, X, Y, Z as follows. Each of the processes W and X reads x from memory, increments by one, stores it to memory, and then terminates. Each of the processes Y and Z reads x from memory, decrements by two, stores it to memory, and then terminates. Each process before reading x invokes the P operation (i.e., wait) on a counting semaphore S and invokes the V operation (i.e., signal) on the semaphore S after storing x to memory. Semaphore S is initialized to two. What is the maximum and minimum possible value of x after all process's complete execution?

**24.** Given a shared variable 'count' initialized to 0, Process P1 increments 'count' by 1, and Process P2 decrements 'count' by 1. If both processes start concurrently and execute the critical section five times each, what is the final value of 'count'?

**25.** Given a system with three threads T1, T2, and T3, and three semaphores S1, S2, and S3 with initial values 1, 2, and 3, respectively. If T1 requires S1, T2 requires S2, and T3 requires S3 to enter their critical sections, in which order will the threads enter their critical sections?

-----

### **Set-3 (Roll No. 31-45)**

**26.** Consider a GLA university computer lab 330 where various students and researchers have access to a shared computing environment. Some students want to use this lab for doing programming assignments and data analysis, while Professors want to utilize this lab to train their deep learning models. Describe which type of operating system in this lab can be utilized that effectively allocates resources, such as CPU time, memory, and peripheral devices, to ensure fairness and optimize productivity among multiple users.

**27.** Predict the output?

```c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
void forkexample()
{
    int x=1;
    if (fork()==0)
        printf("Child has x=%d\n",++x);
    else
        printf("Parent has x=%d\n",--x);
}
int main()
{
    forkexample();
    return 0;
}
```

**28.** Consider the following set of processes that need to be scheduled on a single CPU. All the times are given in milliseconds.

| Process Name | Arrival Time | Execution Time |
| :--- | :--- | :--- |
| A | 0 | 6 |
| B | 3 | 2 |
| C | 5 | 4 |
| D | 7 | 6 |
| E | 10 | 3 |

Using the shortest remaining time first scheduling algorithm, the average process turnaround time (in msec) is?

**29.** For the processes listed in the following table, which of the following scheduling schemes will give the lowest average turnaround time?
a) First Come First Serve
b) Non-preemptive Shortest Job First
c) Shortest Remaining Time

| Process | Arrival Time | Processing Time |
| :--- | :--- | :--- |
| A | 0 | 3 |
| B | 1 | 6 |
| C | 4 | 4 |
| D | 6 | 2 |

**30.** Suppose that the following processes arrive for execution at the times indicated. Each process will run for the amount of time listed. In answering the questions, use nonpreemptive scheduling, and base all decisions on the information you have at the time the decision must be made.

| Process | Arrival Time | Burst Time |
| :--- | :--- | :--- |
| $P_1$ | 0.0 | 8 |
| $P_2$ | 0.4 | 4 |
| $P_3$ | 1.0 | 1 |

a. What is the average turnaround time for these processes with the FCFS scheduling algorithm?
b. What is the average turnaround time for these processes with the SJF scheduling algorithm?
c. The SJF algorithm is supposed to improve performance, but notice that we chose to run process P1 at time 0 because we did not know that two shorter processes would arrive soon. Compute what the average turnaround time will be if the CPU is left idle for the first 1 unit and then SJF scheduling is used. Remember that processes P1 and P2 are waiting during this idle time, so their waiting time may increase. This algorithm could be known as future-knowledge scheduling.

**31.** Consider the following set of processes, with the length of the CPU-burst time given in milliseconds:

| Process | Burst Time | Priority |
| :--- | :--- | :--- |
| P1 | 10 | 3 |
| P2 | 1 | 1 |
| P3 | 2 | 3 |
| P4 | 1 | 4 |
| P5 | 5 | 2 |

The processes are assumed to have arrived in the order P1, P2, P3, P4, P5, all at time 0.
a. Draw four Gantt charts illustrating the execution of these processes using FCFS, SJF, a non-preemptive priority (a smaller priority number implies a higher priority), and RR scheduling.
b. What is the turnaround time of each process for each of the scheduling algorithms in part a?
c. What is the waiting time of each process for each of the scheduling algorithms in part a?

Assume an operating system maps user-level threads to the kernel using the many-to- many model where the mapping is done through LWPs. Furthermore, the system allows the developers to create real-time threads. Is it necessary to bound a real-time thread to an LWP? Explain.

**32.** You are developing an operating system for a personal computer. A user opens a word processing application and starts typing a document. Describe the process creation steps that occur from the user's action to the actual execution of the word processing program.

**33.** In a real-time control system for an autonomous robot, there are multiple processes responsible for sensor data processing, decision-making, and motor control. Describe how you would manage and prioritize processes in different states to ensure the robot's responsiveness to changing environmental conditions.

**34.** A user on a personal computer has opened multiple applications, including a text editor, a web browser, and a media player. Describe how the operating system handles process states such as "Running," "Ready," and "Blocked" to provide a smooth user experience, especially when switching between applications.

**35.** Assume that, you work for a space exploration company, and your team is responsible for programming the software that controls a rover on a distant planet. Your colleague, who is new to this project, asks, "What exactly is a real-time operating system, and why are we using it for the rover's software?" How would you explain the concept of a real-time operating system and its importance in the context of controlling the rover's actions and data processing on a distant planet?

**36.** You are developing a content management system where multiple users can read articles concurrently, but only one user can edit an article at a time. Describe how the Readers-Writers problem applies to this system and outline synchronization strategies to allow concurrent reading while ensuring exclusive access during editing.

**37.** Consider the dining philosopher's problem. If we add a 6th chopstick to the center of the table, have we cured the deadlock problem? If yes, what condition have we removed? If no, explain why not.

-----

### **Set-4 (Roll No. 46-60)**

**38.** Two processes, P1 and P2, need to enter a critical section but must ensure mutual exclusion. Peterson's solution provides a software-based solution using two boolean flags and a turn variable.
a. Explain how Peterson's algorithm ensures mutual exclusion, progress, and bounded waiting.

**39.** Compute the average TAT and average WT for the given data below:

| Process | Arrival Time | Burst Time | Priority |
| :--- | :--- | :--- | :--- |
| P1 | 0 | 11 | 2 |
| P2 | 5 | 28 | 0 |
| P3 | 12 | 2 | 3 |
| P4 | 2 | 10 | 1 |
| P5 | 9 | 16 | 4 |

**40.** The issue of resource utilization shows up in different forms in different types of operating systems. List what resources must be managed carefully in the following settings:
a. Mainframe or minicomputer systems
b. Workstations connected to servers

**41.** Consider three processes, all arriving at time zero, with total execution time of 10, 20 and 30 units respectively. Each process spends the first 20% of execution time doing I/O, the next 70% of time doing computation, and the last 10% of time doing I/O again. The operating system uses a shortest remaining compute time first scheduling algorithm and schedules a new process either when the running process gets blocked on I/O or when the running process finishes its compute burst. Assume that all I/O operations can be overlapped as much as possible. For what percentage of does the CPU remain idle?

**42.** Consider the following processes, with the arrival time and the length of the CPU burst given in milliseconds. The scheduling algorithm used is preemptive shortest remaining-time first.

| Process | Arrival Time | Burst Time |
| :--- | :--- | :--- |
| $P_1$ | 0 | 10 |
| $P_2$ | 3 | 6 |
| $P_3$ | 7 | 1 |
| $P_4$ | 8 | 3 |

The average turnaround time of these processes is \_\_\_\_\_\_\_\_\_\_ milliseconds.

**43.** Consider the following table of arrival time and burst time for three processes P0, P1 and P2.

| Process | Arrival time | Burst Time |
| :--- | :--- | :--- |
| P0 | 0 ms | 9 ms |
| P1 | 1 ms | 4 ms |
| P2 | 2 ms | 9 ms |

The pre-emptive shortest job first scheduling algorithm is used. Scheduling is carried out only at arrival or completion of processes. What is the average waiting time for the three processes?

**44.** Consider the set of 4 processes whose arrival time and burst time are given below-

| Process No. | Arrival Time | CPU Burst | I/O Burst | CPU Burst |
| :--- | :--- | :--- | :--- | :--- |
| P1 | 0 | 2 | 3 | 2 |
| P2 | 4 | 0 | 2 | 1 |
| P3 | 3 | 2 | 1 | 2 |
| P4 | 5 | 2 | 2 | 1 |

If the CPU scheduling policy is Shortest Remaining Time First, calculate the average waiting time and average turnaround time.

**45.** While using your computer, you notice that one application has become unresponsive. Describe how you would use the operating system's task manager or equivalent feature to identify and terminate the unresponsive process.

**46.** How does the FCFS scheduling algorithm work in the context of allocating computers to students in the lab? What are the potential advantages and drawbacks of using FCFS for this purpose?

**47.** Imagine you're leading a team meeting at a software development company. You want to discuss the various types of operating systems and their pros and cons to help your team make informed decisions about which OS to use for their upcoming project. How would you guide the discussion, explaining the different types of operating systems while highlighting their advantages and disadvantages?

**48.** Consider the following C code for process P1 and P2. `a=4` `b=0.` `c=0` (initialization). (GATE-2017)

**P1**

```
if (a<0)
    c=b-a
else
    c=b+a,
```

**P2**

```
b=10
a=-3
```

If the processes P1 and P2 executes concurrently (shared variables a, b and c), What are the be the possible value of 'c' after both processes complete?

**49.** You are tasked with simulating the Dining Philosophers problem, where five philosophers sit around a circular table, and they alternate between thinking and eating. To eat, a philosopher must pick up two forks placed between them and their neighbours. Describe the challenges and potential solutions to ensure that the philosophers do not experience deadlock or resource contention while dining.

-----

### **Set-5 (Roll No. 61-till end)**

**50.** The following C program is executed on a Unix/Linux system:

```c
#include <unistd.h >
int main ()
{
    int i;
    for (i=0; i<10; i++)
        if (i%2==0) fork();
    return 0;
}
```

The total number of child processes created is \_\_\_\_\_\_\_\_\_\_ and Justify your output.

**51.** In a multiprogramming and time-sharing environment, several users share the system simultaneously. This situation can result in various security problems. What are two such problems?

**52.** Assume arrival order is: P1, P2, P3, P4, P5 at time 0, 1, 2, 3, 4 respectively and a smaller priority number implies a higher priority. Draw the Gantt charts for pre-emptive and non-pre-emptive priority scheduling. Calculate Average Turnaround Time and Average Waiting Time.

**53.** Consider a set of 5 processes whose arrival time, CPU time needed and the priority are given below:

| Process number | Arrival time(ms) | CPU time | Priority |
| :--- | :--- | :--- | :--- |
| p1 | 0 | 10 | 5 |
| p2 | 0 | 5 | 2 |
| p3 | 2 | 3 | 1 |
| p4 | 5 | 20 | 4 |
| p5 | 10 | 2 | 3 |

If the CPU scheduling policy is SJF, the average waiting time (with preemption) will be?

**54.** Find the waiting time of P4 process using priority scheduling algorithm (Assume lowest number has highest priority).

| Process | P1 | P2 | P3 | P4 | P5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Burst time** | 5 | 13 | 8 | 6 | 12 |
| **Priority** | 1 | 3 | 0 | 4 | 2 |

**55.** The traditional UNIX scheduler enforces an inverse relationship between priority numbers and priorities: the higher the number, the lower the priority. The scheduler recalculates process priorities once per second using the following function: Priority = (recent CPU usage / 2) + base where base = 60 and recent CPU usage refers to a value indicating how often a process has used the CPU since priorities were last recalculated. Assume that recent CPU usage for process P1 is 40, for process P2 is 18, and for process P3 is 10. What will be the new priorities for these three processes when priorities are recalculated? Based on this information, does the traditional UNIX scheduler raise or lower the relative priority of a CPU-bound process?

**56.** You are designing a task scheduler for an operating system that supports both foreground and background tasks. Explain how the "Ready" and "Running" states are managed in the context of a multi-core CPU, and how the scheduler decides which process to move from "Ready" to "Running."

**57.** In a multi-user operating system, several users are running CPU-bound tasks. One user has a high-priority task, while the others have lower-priority tasks. Explain how a priority-based scheduling algorithm would handle this situation and its potential advantages and drawbacks.

**58.** In a computer lab, there are multiple student workstations running various applications. A student is complaining that their computer is running slowly because of a CPU-intensive application running on another workstation. How could a CPU scheduler address this issue and ensure fair CPU allocation among all users?

**59.** Consider three concurrent processes P1, P2 and P3 as shown below, which access a shared variable D that has been initialized to 100.

| P1 | P2 | P3 |
| :--- | :--- | :--- |
| : | : | : |
| : | : | : |
| D = D + 20 | D = D - 50 | D = D + 10 |
| : | : | : |
| : | : | : |

The processes are executed on a uniprocessor system running a time-shared operating system. If the minimum and maximum possible values of D after the three processes have completed execution are X and Y respectively, then the value of Y-X is \_\_\_\_\_\_\_\_\_\_.

**60.** The following program consists of 3 concurrent processes and 3 binary semaphores. The semaphores are initialized as `S0=1`, `S1=0`, `S2=0`.

**Process P0**

```
while(true)
{
    wait(S0);
    print '0';
    release(S1);
    release(S2);
}
```

How many times will P0 print '0'?