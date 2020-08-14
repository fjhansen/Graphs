import random
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.name)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_users(self):
        print(self.users)

    def populate_graph(self, num_users, avg_friendships):

        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # For loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # matches up users
        
        # Scale Testing
        
        # Create friendships
        # To create N random friendships,
        # create a list with all possible friendship combos
        # shuffle combo list, then grab first N elements from combo list
        # import random to get shuffle
        
        possible_friendships = []
        for user_id in self.users:
            #this grabs all the users after the current user
            # also grabs the actual last ID in the list of users
            for friend_id in range(user_id + 1, self.last_id +1):
            # this appends a tuple of user_id+1 and the current iteration
                possible_friendships.append((user_id, friend_id))
        #print("P_F: \n",possible_friendships)

        # fischer gates shuffle

        random.shuffle(possible_friendships)

        print("P_F: \n",possible_friendships)

        # Create n friendships where n = avg_friendships * num_users //2
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users

        # this creates our 10 users with an average of 2 friendships each
        for i in range(num_users * avg_friendships //2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


        # we want to view people in the extended social network
        # people in extended social network can be compared to connected components
        # to do this we will use a breadth or depth first traversal

        # we want to see the path between two users and how long the path is
        # each edge represents a friendship

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # BFT AND BFS
        # Doing a BF Traversal but also storing the path

        # create a queue
        q = Queue()
        # enq a path to the starting user_id
        q.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set
        # while q is not empty
        while q.size() > 0:
        # deq first path
            path = q.dequeue()
            # last id from path
            current_id = path[-1]
            # check if its been cisited
            if current_id not in visited:
            # if not
                # add it to visited along with path
                visited[current_id] = path
                # enq the path to each friend to the q
                for friend_id in self.friendships[current_id]:
                    # copy path
                    path_copy = path.copy()
                    # append each neighbor
                    path_copy.append(friend_id)
                    # enq
                    q.enqueue(path_copy)
        return visited


# Questions

# 1. To create 100 users with an average of 10 friends each...
# 500 is the answer. You would multiply the total of users with average of friends divided by two.

# 2.
# 

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    #sg.get_users()
    print("\n Friendships: \n",sg.friendships)
    print("\n Users: \n",sg.users)
    connections = sg.get_all_social_paths(1)
    print("\n Connections: \n",connections)
