import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class PartA {
    
    private static class Process {
        String id;
        String resources;
        Process next;

       public Process(String id, String resources) {
            this.id = id;
            this.resources = resources;
            this.next = null;
        }

        @Override
        public String toString() {
            return id + " " + resources;
        }
    }

    private static class ProcessQueue {
        private Process head;
        private Process tail;
        private int size;

        public ProcessQueue() {
            //Default values for the Linked lists for processing and waiting queues 
            this.head = null;
            this.tail = null;
            this.size = 0;
        }

        public void addProcess(Process process) {
            if (tail == null) {
                head = process;
                tail = process;
            } else {
                tail.next = process;
                tail = process;
            }
            size++;
        }

        public Process pollProcess() {
            if (head == null) {
                return null;
            }
            Process process = head;
            head = head.next;
            if (head == null) {
                tail = null;
            }
            size--;
            return process;
        }

        public boolean isEmpty() {
            return head == null;
        }

        public int getSize() {
            return size;
        }
    }

    private static boolean executeProcess(Process process, boolean resourceA, boolean resourceB, boolean resourceC) {
        for (char resource : process.resources.toCharArray()) { //converts the resource to char and makes sure it 
            //if one is resoruce being used, then it would return false then line 121 won't meet condition until the cycle is completed
            if (resource == 'A' && !resourceA) return false; 
            if (resource == 'B' && !resourceB) return false;
            if (resource == 'C' && !resourceC) return false;
        }
        //Until all resources have been used then the program will return and then can execute 
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); //Used for taking the input by line 
        ProcessQueue processQueue = new ProcessQueue(); //Creates an instance variable processQueue of ProcessQueue 

        System.out.println("Enter processes and resources: "); 
        String entry = input.nextLine(); //Used for taking the input by line 

        // Parse input to string 
        String[] processStrings = entry.split(";"); //Splits by ; [P1(A), P2(B) etc]
        for (String processString : processStrings) {
            String[] parts = processString.split("\\("); //splits each process and queue into a list, e.g: [P1, A)] 
            String id = parts[0]; //ID is the 
            String resources = parts[1].replaceAll("[\\)\\s]", "");//removes all other brackets from the resources
            processQueue.addProcess(new Process(id, resources)); //adds the process into the id 
        }
        // For resource availability, we assume they are true for each (A,B,C)
        boolean resourceA = true;
        boolean resourceB = true;
        boolean resourceC = true;

        int cycleCount = 0; //Count for tracking the cycles 
        Queue<Process> waitingQueue = new LinkedList<>(); //Using FIFO concept, to create a temporary waiting queue for storing the Process types
                                                          //Until resources are complete   
        while (!processQueue.isEmpty() || !waitingQueue.isEmpty()) { //Looping until the process queue and the waiting queues are empty
            cycleCount++; 
            System.out.println("Cycle " + cycleCount + ": Process Queue Size: " + processQueue.getSize());

            // Move all processes from processQueue to waitingQueue
            while (!processQueue.isEmpty()) { 
                waitingQueue.add(processQueue.pollProcess()); //shift the remaining processes, return the first waiting process to 
            }
            // Check waiting queue and execute processes that can start
            int waitingQueueSize = waitingQueue.size();
            for (int i = 0; i < waitingQueueSize; i++) {
                Process currentProcess = waitingQueue.poll();
                if (executeProcess(currentProcess, resourceA, resourceB, resourceC)) {
                    System.out.println("Executing: " + currentProcess + " at Cycle " + cycleCount);
                
                    // Simulate resource allocation for one cycle
                    if (currentProcess.resources.contains("A")) resourceA = false;
                    if (currentProcess.resources.contains("B")) resourceB = false;
                    if (currentProcess.resources.contains("C")) resourceC = false;
                } else {
                    //If the resources being used, then the following process will wait until the cycle has been completed 
                    System.out.println("Waiting: " + currentProcess + " at Cycle " + cycleCount);
                    processQueue.addProcess(currentProcess); // Add back to the process queue for the next cycle
                }
            }
            //Simulate resource availability update after one cycle
            //Resources are available after being used in the cycle 
            resourceA = true; 
            resourceB = true;
            resourceC = true;
        }
        //System.out.println("Total processes executed: " + totalProcesses);
        System.out.println("Total cycles: " + cycleCount); 
        input.close();
    }
}

