## Arthrex_coding_assignment
#problem statement:
Let us assume that Arthrex wants to hire an intern.
The recruiter from Arthrex starts gathering a list of interns from its database.
In order to keep the hiring pipeline healthy, every time a recruiter calls up a candidate
to schedule an interview, he also asks the candidate to provide a list of his
classmates.
Write a program in a language of your choice to list all the candidates that could be
contacted by the above method, until a candidate is hired or the complete list of
candidates along with their classmates is exhausted.

Data Structure
The data dictionary represents the relationships among the candidates. Each key is a candidate, and the corresponding value is a list of their friends.

How It Works
Input: The user provides the name of the starting candidate.
Handling Unlisted Candidates: If a candidate does not have any friends listed in the data dictionary, the program searches for this candidate in the lists of other candidates and continues the traversal from there.
Output: The program outputs the list of contacted candidates in the order they were contacted.

#Running the Program
1.Clone the repository or download the contact_traversal.py file.
2.Open a terminal or command prompt.
3.Navigate to the directory where the 'coding_assignment.py' file is located.
4.Run the program by executing the following command:
                                                  python coding_assignment.py

5.When prompted, enter the name of the starting candidate (a single letter from A-Z) and press Enter.
6.The program will output the list of contacted candidates in the order they were contacted.
                        $ python contact_traversal.py
                         Enter person's name to select for the job (letters from A-Z): M
                         M, K, L, N, A, B, C, J, V, W, X, Y, Z

##Approach
1. Data Initialization: A dictionary (data) is used to represent the relationships among the candidates.

2.Function Definition:
get_contacts(person, contact=[]): A recursive function that performs a depth-first search (DFS) traversal.
It adds the person to the contact list if they have not been contacted yet.
It recursively calls itself for each friend of the person.
If the person does not have any friends listed, it searches for the person in the lists of other candidates and continues the traversal.

3.User Input: The user is prompted to enter the starting candidate.

4.Output: The program prints the list of contacted candidates.
                                                  


