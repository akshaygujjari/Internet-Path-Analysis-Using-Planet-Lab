# Internet-Path-Analysis-Using-Planet-Lab
The objective of this project is to experiment with real, worldwide Internet testbed, to gather first-hand measurements of Internet performance from geographically distributed machines and evaluate path properties in today’s Internet.

In this project, I implemented a simple Internet measurement framework in which a minimum of 10 PlanetLab nodes will perform periodic pairwise path measurements using ping (with 20 packets) and traceroute. The measurement data is collected over the course of at least two weeks.

The measurement nodes store ping and traceroute logs locally after each measurement. Once all of the measurements are completed I analyzed the measurements based on various factors using python. The overall project is based on the reasearch works of Vern Paxson [http://conferences.sigcomm.org/sigcomm/1996/papers/paxson.pdf] 


Project Objective
1. Creating a PlanetLab account
2. Getting a slice
 2.1. Adding nodes to the slice
3. Accessing PlanetLab nodes
4. Measurement utilities
5. Running utilities periodically
6. Analysis
    6.1 Implement measurements and data collection
    6.2 Implement data analysis - As we end up with a lot of unstructured and unwanted data


A project report with step by step explanation, process, results is available upon request. If needed email me on gujjariakshay@gmail.com  
