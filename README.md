# High-Performance-Python
+ Explore different ways to extend python with high performance tools to enhance performance of the system.


    + CPU :
    The main properties of interest in a computing unit are the number of operations it can do in one cycle
    and the number of cycles it can do in one second. The first value is measured by its instructions per cycle (IPC),
    while the latter value is measured by its clock speed. These two measures are always competing with each other when new computing units are being made.
    For example, the Intel Core series has a very high IPC but a lower clock speed, while the Pentium 4 chip has the reverse.
    GPUs, on the other hand, have a very high IPC and clock speed, but they suffer from other problems like the slow communications that we discuss
    in “Communications Layers”.


    In general, computing units have advanced quite slowly over the past decade (see Figure 1-1). Clock speeds and IPC have both been
    stagnant because of the physical limitations of making transistors smaller and smaller. As a result, chip manufacturers have been
    relying on other methods to gain more speed, including simultaneous multithreading (where multiple threads can run at once), more
    clever out-of-order execution, and multicore architectures.

    + Multithreading :
    Hyperthreading presents a virtual second CPU to the host operating system (OS), and clever hardware logic tries to interleave two threads of
    instructions into the execution units on a single CPU. When successful, gains of up to 30% over a single thread can be achieved. Typically,
    this works well when the units of work across both threads use different types of execution units—for example, one performs floating-point
    operations and the other performs integer operations.

    + Python Problem with Multicore programming :
    Furthermore, a major hurdle with utilizing multiple cores in Python is Python’s use of a global interpreter lock (GIL). The GIL makes sure that a
    Python process can run only one instruction at a time, regardless of the number of cores it is currently using. This means that even though some
    Python code has access to multiple cores at a time, only one core is running a Python instruction at any given time. Using the previous example of
    a survey, this would mean that even if we had 100 question askers, only one person could ask a question and listen to a response at a time. This
    effectively removes any sort of benefit from having multiple question askers! While this may seem like quite a hurdle, especially if the current
    trend in computing is to have multiple computing units rather than having faster ones, this problem can be avoided by using other standard library
    tools, like multiprocessing, technologies like numpy or numexpr, Cython, or distributed models of computing.


    Memory Units
    For example, most memory units perform much better when they read one large chunk of data as opposed to many small chunks (this is referred to as
    sequential read versus random data). If the data in these memory units is thought of as pages in a large book, this means that most memory units have
    better read/write speeds when going through the book page by page rather than constantly flipping from one random page to another. While this fact
    is generally true across all memory units, the amount that this affects each type is drastically different.

    Here is a short description of the various memory units that are commonly found inside a standard workstation, in order of read/write speeds:2

    Spinning hard drive
    Long-term storage that persists even when the computer is shut down. Generally has slow read/write speeds because the disk must be physically spun and moved.
    Degraded performance with random access patterns but very large capacity (10 terabyte range).

    Solid-state hard drive
    Similar to a spinning hard drive, with faster read/write speeds but smaller capacity (1 terabyte range).

    RAM
    Used to store application code and data (such as any variables being used). Has fast read/write characteristics and performs well with random access patterns,
    but is generally limited in capacity (64 gigabyte range).

    L1/L2 cache
    Extremely fast read/write speeds. Data going to the CPU must go through here. Very small capacity (megabytes range).

    ++ Many modes of communication exist, but all are variants on a thing called a bus :
    The frontside bus, for example, is the connection between the RAM and the L1/L2 cache. It moves data that is ready to be transformed by the processor into the
    staging ground to get ready for calculation, and it moves finished calculations out. There are other buses, too, such as the external bus that acts as the main
    route from hardware devices (such as hard drives and networking cards) to the CPU and system memory. This external bus is generally slower than the frontside bus.


    Network Communication :
    In addition to the communication blocks within the computer, the network can be thought of as yet another communication block. This block, though, is much more
    pliable than the ones discussed previously; a network device can be connected to a memory device, such as a network attached storage (NAS) device or another computing
    block, as in a computing node in a cluster. However, network communications are generally much slower than the other types of communications mentioned previously.
    While the frontside bus can transfer dozens of gigabits per second, the network is limited to the order of several dozen megabits.

    IDEALIZED COMPUTING
    When the code starts, we have the value of number stored in RAM. To calculate sqrt_number, we need to send the value of number
    to the CPU. Ideally, we could send the value once; it would get stored inside the CPU’s L1/L2 cache, and the CPU would do the calculations and then send the values
    back to RAM to get stored.
    This scenario is ideal because we have minimized the number of reads of the value of number from RAM, instead opting for reads from the

    $ python -m cProfile -o fib.prof fib.py
    $ pip3 install snakeviz --user

    $ snakeviz fib.profile
