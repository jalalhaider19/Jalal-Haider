import java.util.LinkedList;
import java.util.List;
import java.util.Random;

public class processSimulation {
    public static void main(String[] args) {
        List<Integer> processes = new LinkedList<>(); //creates a list of processes in a chain 
        Random random = new Random(); //random instantiated from Random

        // Initialize the process list with 20 processes
        for (int i = 0; i < 20; i++) {
            processes.add(random.nextInt(1,4) + 1);
        }
        //Provides a counter to go through the lest of processes 
        int cycle = 0;

        while (cycle < 1000 && !processes.isEmpty()) {
            cycle++;
            
            // Execute processes with the randomnly assigned
            List<Integer> resources = new LinkedList<>(); //creates another list of resources (1,2,3)
            for (int process : processes) {
                resources.add(random.nextInt(3) + 1); //adding random resources, from 1,2,3
            }

            // Remove completed processes until the list is to be empty every cycle 
            for (int i = resources.size() - 1; i >= 0; i--) {
                if (resources.get(i) >= processes.get(i)) {
                    processes.remove(i);
                }
            }

            // Add 2 new processes with random resources
            for (int i = 0; i < 2; i++) {
                processes.add(random.nextInt(1,4) + 1);
            }

            // Output the length of the process list every 100 cycles to see the growth 
            if (cycle % 100 == 0) {
                System.out.println("Length of processes at cycle " + cycle + ": " + processes.size());
                System.out.println(); 
            }
        }

        // Output the number of processes left after 1000 cycles
        if (cycle == 1000) {
            System.out.println("We have a total of " + processes.size() + " left.");
        } else {
            System.out.println("All processes completed in " + cycle + " cycles.");
        }
    }
}







