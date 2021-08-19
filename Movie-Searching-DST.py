import vlc
import pafy
import time


class DoulbeNode:

    # Constructor to create a new node
    def __init__(self, year, title, duration, rating, cast):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.cast = cast
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Function to merge two linked list
    def merge(self, first, second):

        # If first linked list is empty
        if first is None:
            return second

            # If secon linked list is empty
        if second is None:
            return first

            # Pick the smaller value
        if first.year < second.year:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

            # Function to do merge sort

    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead

        second = self.split(tempHead)

        # Recur for left and righ halves
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)

        # Merge the two sorted halves
        return self.merge(tempHead, second)

        # Split the doubly linked list (DLL) into two DLLs

    # of half sizes
    def split(self, tempHead):
        fast = slow = tempHead
        while (True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

        # Given a reference to the head of a list and an

    # integer,inserts a new node on the front of list
    def push(self, year, title, duration, rating, cast):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = DoulbeNode(year, title, duration, rating, cast)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

            # 5. move the head to point to the new node
        self.head = new_node

    def printList(self, node):
        print("MOVIE")
        while (node is not None):
            print("YEAR OF RELEAESE")
            print(" ")
            print(node.year)
            print(" ")
            print("MOVIE NAME")
            print(" ")
            print(node.title)
            print(" ")
            print("DURATION")
            print(" ")
            print(node.duration)
            print(" ")
            print("RATINGS")
            print(" ")
            print(node.rating)
            print(" ")
            print("CASTING OF THE MOVIE")
            print(" ")
            print(node.cast)
            print(" ")
            node = node.next
            print("\n")


class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s


class TreeNode:
    def __init__(self, year=None, title=None, duration=None, rating=None, arr=[]):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.left = None
        self.right = None
        self.arr = arr


class BST:
    def __init__(self):
        self.root = None

    def insert(self, year, title, duration, rating, arr=[]):
        if self.root is None:
            self.root = TreeNode(year, title, duration, rating, arr)
        else:
            self._insert(year, title, duration, rating, arr, self.root)

    def _insert(self, year, title, duration, rating, arr, cur_node):
        if title != cur_node.title and title < cur_node.title:
            if cur_node.left is None:
                cur_node.left = TreeNode(year, title, duration, rating, arr)
                cur_node.left.parent = cur_node
            else:
                self._insert(year, title, duration, rating, arr, cur_node.left)

        elif title != cur_node.title and title > cur_node.title:
            if cur_node.right is None:
                cur_node.right = TreeNode(year, title, duration, rating, arr)
                cur_node.right.parent = cur_node
            else:
                self._insert(year, title, duration, rating, arr, cur_node.right)
        else:
            print("Movie Is Already In The Storage!")

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
            return True

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print("---------------------MOVIE DETAILS---------------------------")
            print("THE RELEASE YEAR OF THE MOVIE:" + "\n" + str(cur_node.year))

            print("THE TITLE  OF THE MOVIE:" + "\n" + str(cur_node.title))

            print("THE  RATING OF THE MOVIE:" + "\n" + str(cur_node.rating))

            print("THE DURATION OF THE MOVIE:" + "\n" + str(cur_node.duration))

            print("THE Cast OF THE MOVIE:")
            print("\n")
            cur_node.arr.print_list()
            print("\n")
            print("----------------------------------------------------------")
            self._inorder_print_tree(cur_node.right)

    dbl = DoublyLinkedList()
    dbl2 = DoublyLinkedList()
    dbl3 = DoublyLinkedList()

    def _find(self, title, cur_node):

        if title > cur_node.title and cur_node.right:
            return self._find(title, cur_node.right)
        elif title < cur_node.title and cur_node.left:
            return self._find(title, cur_node.left)
        if title == cur_node.title:
            print("THE RELEASE YEAR OF THE MOVIE:" + "\n" + str(cur_node.year))
            print("THE TITLE  OF THE MOVIE:" + "\n" + str(cur_node.title))
            print("THE  RATING OF THE MOVIE:" + "\n" + str(cur_node.rating))
            print("THE DURATION OF THE MOVIE:" + "\n" + str(cur_node.duration))
            print("THE Cast OF THE MOVIE:")
            print("\n")
            cur_node.arr.print_list()

            print("\n")

    def find(self, title):
        if self.root:
            is_found = self._find(title, self.root)
            if is_found:
                return self._find(title, self.root)
            return False
        else:
            return None

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def year(self, year):
        if self.root:
            self._year(self.root, year)
            return False

    def _year(self, cur_node, year):

        if cur_node:

            self._year(cur_node.left, year)

            if cur_node.year == year:
                print("---------------------MOVIES RELEASE IN THE YEAR", f"{year}  ---------------------------")
                print("\n")
                print("THE RELEASE YEAR OF THE MOVIE:" + "\n" + str(cur_node.year))
                print("\n")
                print("THE TITLE  OF THE MOVIE:" + "\n" + str(cur_node.title))
                print("\n")
                print("THE  RATING OF THE MOVIE:" + "\n" + str(cur_node.rating))
                print("\n")
                print("THE DURATION OF THE MOVIE:" + "\n" + str(cur_node.duration))
                print("\n")
                print("THE Cast OF THE MOVIE:")
                print("\n")
                cur_node.arr.print_list()

                print("\n")
                self.dbl3.push(cur_node.year, cur_node.title, cur_node.duration, cur_node.rating, cur_node.arr.show())
            self._year(cur_node.right, year)

    def ratings(self, rating):
        if self.root:
            self._ratings(self.root, rating)
            return False

    def _ratings(self, cur_node, rating):

        if cur_node:
            self._ratings(cur_node.left, rating)

            if cur_node.rating == rating:
                print("\n")
                print("THE RELEASE YEAR OF THE MOVIE:" + "\n" + str(cur_node.year))
                print("\n")
                print("THE TITLE  OF THE MOVIE:" + "\n" + str(cur_node.title))
                print("\n")
                print("THE  RATING OF THE MOVIE:" + "\n" + str(cur_node.rating))
                print("\n")
                print("THE DURATION OF THE MOVIE:" + "\n" + str(cur_node.duration))
                print("\n")
                print("THE Cast OF THE MOVIE:")
                print("\n")
                cur_node.arr.print_list()
                print("\n")
                self.dbl2.push(cur_node.year, cur_node.title, cur_node.duration, cur_node.rating, cur_node.arr.show())
            self._ratings(cur_node.right, rating)

    def duoyear(self, Iyear, Fyear):

        if self.root:
            self._duoyear(self.root, Iyear, Fyear)

            return ("NO MOVIES AVAILIBLE")

    def _duoyear(self, cur_node, Iyear, Fyear):

        if cur_node:

            self._duoyear(cur_node.left, Iyear, Fyear)
            if cur_node.year >= Iyear:

                if cur_node.year <= Fyear:
                    print("\n")
                    print("THE RELEASE YEAR OF THE MOVIE:" + "\n" + str(cur_node.year))
                    print("\n")
                    print("THE TITLE  OF THE MOVIE:" + "\n" + str(cur_node.title))
                    print("\n")
                    print("THE  RATING OF THE MOVIE:" + "\n" + str(cur_node.rating))
                    print("\n")
                    print("THE DURATION OF THE MOVIE:" + "\n" + str(cur_node.duration))
                    print("\n")
                    print("THE Cast OF THE MOVIE:")
                    print("\n")
                    cur_node.arr.print_list()

                    print("\n")
                    self.dbl.push(cur_node.year, cur_node.title, cur_node.duration, cur_node.rating,
                                  cur_node.arr.show())

            self._duoyear(cur_node.right, Iyear, Fyear)

    def __deleteNodeHelper(self, node, key):
        if node == None:
            return node
        elif key < node.title:
            node.left = self.__deleteNodeHelper(node.left, key)
        elif key > node.title:
            node.right = self.__deleteNodeHelper(node.right, key)
        else:
            if node.left == None and node.right == None:
                node = None
            elif node.left == None:
                temp = node
                node = node.right
            elif node.right == None:
                temp = node
                node = node.left
            else:
                temp = self.minimum(node.right)
                node.title = temp.title
                node.right = self.__deleteNodeHelper(node.right, temp.data)
        return node

    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def deleteNode(self, data):
        print("Movie Deleted Succesfully")
        return self.__deleteNodeHelper(self.root, data)

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

    def show(self):

        count = []
        cur_node = self.head

        while cur_node:
            count.append(cur_node.data)
            cur_node = cur_node.next
        return count

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None


arripman = "https://youtu.be/BmkvuHpfrkk"
arrTransformersDarkKnight = "https://youtu.be/AntcyqJ6brc"
arrFindingnemo = "https://youtu.be/2zLkasScy7A"
arrKiller = "https://youtu.be/IrzSCkAaAbQ"
arrAlien = "https://youtu.be/svnAD0TApb8"
arrAmericanSniper = "https://youtu.be/99k3u9ay1gs"
arrTerminator = "https://youtu.be/k64P4l2Wmeg"
arrJaws3 = "https://youtu.be/PNZeHf7RpKE"
arrFastAndFurios = "https://youtu.be/2TAOizOnNPo"
arrTheInternship = "https://youtu.be/cdnoqCViqUo"
arrBabyDriver = "https://youtu.be/D9YZw_X5UzQ"
arrMissionImpossible = "https://youtu.be/Ohws8y572KE"
arrBirdBox = "https://youtu.be/o2AsIXSh2xo"
arrMillionDollarBaby = "https://youtu.be/5_RsHRmIRBY"
arrIpMan3 = "https://youtu.be/_wUcbN34leM"
arrTheDarkKnightRises = "https://youtu.be/g8evyE9TuYk"
arrManOfSteel = "https://youtu.be/GokKUqLcvD8"
arrTheInception = "https://youtu.be/YoHD9XEInc0"
arrShutterIsland = "https://youtu.be/5iaYLCiq5RM"
arrTheGodFather = "https://youtu.be/sY1S34973zA"
arrIronman = "https://youtu.be/8ugaeA-nMTc"
arrConjuring = "https://youtu.be/ejMMn0t58Lc"
arrCaptianAmericaWinterSolider = "https://youtu.be/7SlILk2WMTI"
arrPredator = "https://youtu.be/WaG1KZqrLvM"
arrTaken = "https://youtu.be/uPJVJBm9TPA"
arrBadBoys3 = "https://youtu.be/hbaUcwjshOs"
arrAvengersInfinityWar = "https://youtu.be/6ZfuNTqbHE8"
arrFastAndFurios8 = "https://youtu.be/uisBaTkQAEs"
arrShapeOfWater = "https://youtu.be/XFYWazblaUA"
arrBabylyon = "https://youtu.be/OpNX6Qlq67k"
arrTheShining = "https://youtu.be/S014oGZiSdI"
arrTheSixthSense = "https://youtu.be/3-ZP95NF_Wk"
arrShawasankRedemtion = "https://youtu.be/NmzuHjWmXOc"
arrRocky = "https://youtu.be/I2zFQmHWVCI"
arrDriver = "https://youtu.be/R_1wvCJRArU"
arrJusticeLeague = "https://youtu.be/3cxixDgHUYw"
arrDeparted = "https://youtu.be/iojhqm0JTW4"
arrParasite = "https://youtu.be/5xH0HfJHsaY"
arrToyStory = "https://youtu.be/rNk1Wi8SvNc"
arrSchindlerList = "https://youtu.be/gG22XNhtnoY"
arrPulpFiction = "https://youtu.be/s7EdQ4FqbhY"
arrFightClub = "https://youtu.be/qtRKdVHc-cE"
arrJoker = "https://youtu.be/-_DJEzZk2pc"
arrForrestGump = "https://youtu.be/uPIEn0M8su0"
arrTheMatrix = "https://youtu.be/vKQi3bBA1y8"
arrGoodfellas = "https://youtu.be/2ilzidi_J8Q"
arrSevenSamurai = "https://youtu.be/wJ1TOratCTo"
arrSeven = "https://youtu.be/znmZoVkCjpI"
arrCityofGod = "https://youtu.be/dcUOO4Itgmw"
arrLifeIsBeautiful = "https://youtu.be/pAYEQP8gx3w"
arrSpiritedAway = "https://youtu.be/ByXuk9QqQkk"
arrStreetfighter = "https://youtu.be/xliSIBRD0C0"
arrTheGreenMile = "https://youtu.be/Ki4haFrqSrw"
arrHarryPotterandtheDeathlyHallowsPart2 = "https://youtu.be/monOjieIgA4"
arrAngelique = "https://youtu.be/A6cFA0u5_Io"
arrMeetJoeBlack = "https://youtu.be/_zIOjl93WrU"
arrTheNotebook = "https://youtu.be/FC6biTjEyZw"
arrQuantumofSolace = "https://youtu.be/f6acw690AqQ"
arrCocoBeforeChanel = "https://youtu.be/isEnyrd2Moc"
arrMemoirsofaGeisha = "https://youtu.be/4L-xlmakQvc"
arrArmageddon = "https://youtu.be/kg_jH47u480"
arrPiratesoftheCaribbeanAtWorldsEnd = "https://youtu.be/HKSZtp_OGHY"
arrCasinoRoyale = "https://youtu.be/36mnx8dBbGE"
arrTransformers = "https://youtu.be/dxQxgAfNzyE"
arrBasicInstinct = "https://youtu.be/4f96x3UpoaQ"
arrBeyondBorders = "https://youtu.be/C98QNRlQgZ8"
arrTheTwilightSagaBreakingDawnPart2 = "https://youtu.be/5xOSoONDpY4"
arrXMenTheLastStand = "https://youtu.be/V75dMMIW2B4"
arrTheLordoftheRingsTheFellowshipoftheRing = ""
arrTheLordoftheRingsTheTwoTowers = "https://youtu.be/LbfMDwc4azU"
arrTheAvengers = "https://youtu.be/eOrNdBpGMv8"
arrShrek = "https://youtu.be/CwXOrWvPBPk"
arrSpiderMan = "https://youtu.be/Nt9L1jCKGnE"
arrTheBookofEli = "https://youtu.be/zSMHmtaoXtI"
arrIAmLegend = "https://youtu.be/dtKMEAXyPkg"
arrMinorityReport = "https://youtu.be/lG7DGMgfOb8"
arrVanillaSky = "https://youtu.be/k09OX40NLUw"
arrEnough = "https://youtu.be/L1WWhWsvOZg"
arrInHerShoes = "https://youtu.be/ws3QUUyoNhU"
arrTheHoliday = "https://youtu.be/BDi5zH18vxU"
arrPearlHarbor = "https://youtu.be/oGYcxjywx0o"
arrHesJustNotThatIntoYou = "https://youtu.be/2c3rxHgfRTo"
arrABeautifulMind = "https://youtu.be/9wZM7CQY130"
arrCinemaParadiso = "https://youtu.be/C2-GX0Tltgw"
arrTheBreakUp = "https://youtu.be/ljnEUL-fdt0"
arrDearJohn = "https://youtu.be/r0fq5dd0C60"
arrIronMan3 = "https://youtu.be/Ke1Y3P9D0Bc"
arrApocalypseNow = "https://youtu.be/FTjG-Aux_yQ"
arrMemento = "https://youtu.be/HDWylEQSwFo"
arrJhonWick = "https://youtu.be/C0BMx-qxsP4"
arrRituals = "https://youtu.be/Vfugwq2uoa0"
arrLooper = "https://youtu.be/2iQuhsmtfHw"
arrJurassicPark = "https://youtu.be/lc0UehYemQA"
arrBlackPanther = "https://youtu.be/xjDjIWPwcPU"
arrGladiator = "https://youtu.be/owK1qxDselE"
arrExtraction = "https://youtu.be/L6P3nI6VnlY"
arrSkyfall = "https://youtu.be/6kw1UVovByw"
arrNightCrawler = "https://youtu.be/u1uP_8VJkDQ"
arrSourceCode = "https://youtu.be/mnJegNyAb1w"
arrNonStop = "https://youtu.be/jiHDJ19A3dk"

bst = BST()
IpMan = LinkedList()
IpMan.append("Don Yen")
IpMan.append("Mishi Kisha")
IpMan.append("Mike Tyson")
IpMan.append("Slynder Jack")
IpMan.append("Magin Foster")
IpMan.append("Morgan Freeman")
Findingnemo = LinkedList()
Findingnemo.append("ALBERT BROOKS")
Findingnemo.append("ALEXENDER GLOUD")
Findingnemo.append("ELEN DEGENERS")
Findingnemo.append("ANDREW STANTON")
Findingnemo.append("WILLAM DEFOE")
Killer = LinkedList()
Killer.append("PAUL WESSLEY")
Killer.append("TORIE DEVITTO")
Killer.append("LEIGHTEN MEESTER")
Killer.append("KALLLEY CUCUO")
Killer.append("ROBERT BUCKLEY")
Killer.append("JC CHASEZ")
Alien = LinkedList()
Alien.append("Sigourney Weaver")
Alien.append("Carrie Henn ")
Alien.append("Michael Biehn ")
Alien.append("Lance Henriksen ")
Alien.append("Paul Reiser")
AmericanSniper = LinkedList()
AmericanSniper.append("Bradley Cooper ")
AmericanSniper.append("Kyle Gallner ")
AmericanSniper.append("Cole Konis ")
AmericanSniper.append("Ben Reed ")
AmericanSniper.append("Elise Robertson ")
Terminator = LinkedList()
Terminator.append("Arnold Schwarzenegger")
Terminator.append("Michael Biehn")
Terminator.append("Linda Hamilton")
Terminator.append("Paul Winfield")
Terminator.append("Lance Henriksen")
Jaws3 = LinkedList()
Jaws3.append("Dennis Quaid")
Jaws3.append("Bess Armstrong")
Jaws3.append("Simon MacCorkindale")
Jaws3.append("Louis Gossett Jr.")
Jaws3.append("John Putch")
FastAndFurios = LinkedList()
FastAndFurios.append("Paul Walker")
FastAndFurios.append("Vin Diesel")
FastAndFurios.append("Michelle Rodriguez")
FastAndFurios.append("Jordana Brewster")
FastAndFurios.append("Rick Yune")
TheInternship = LinkedList()
TheInternship.append("Vince Vaughn ")
TheInternship.append("Owen Wilson ")
TheInternship.append("Rose Byrne ")
TheInternship.append("Max Minghella ")
TheInternship.append("Aasif Mandvi ")
BabyDriver = LinkedList()
BabyDriver.append("Ansel Elgort ")
BabyDriver.append("Jon Bernthal ")
BabyDriver.append("Jon Hamm")
BabyDriver.append("Eiza Gonzelez ")
BabyDriver.append("Gomezz Helen")
MissionImpossible = LinkedList()
MissionImpossible.append("Tom Cruise ")
MissionImpossible.append("Jon Voight ")
MissionImpossible.append("Henry Czerny ")
MissionImpossible.append("Emmanuelle Baart ")
MissionImpossible.append("Jean Reno ")
BirdBox = LinkedList()
BirdBox.append("Sandra Bullock ")
BirdBox.append("Trevante Rhodes ")
BirdBox.append("John Malkovich ")
BirdBox.append("Sarah Paulson ")
BirdBox.append("Jacki Weaver ")
MillionDollarBaby = LinkedList()
MillionDollarBaby.append("Clint Eastwood ")
MillionDollarBaby.append("Hilary Swank ")
MillionDollarBaby.append("Morgan Freeman")
MillionDollarBaby.append("Jay Baruchel ")
MillionDollarBaby.append("Mike Colter ")
IpMan3 = LinkedList()
IpMan3.append("Donnie Yen ")
IpMan3.append("Lynn Xiong ")
IpMan3.append("Jin Zhang ")
IpMan3.append("Mike Tyson")
IpMan3.append("Patrick Tam ")
IpMan3.append("Karena Ng ")
TheDarkKnightRises = LinkedList()
TheDarkKnightRises.append("Christian Bale ")
TheDarkKnightRises.append("Gary Oldman ")
TheDarkKnightRises.append("Tom Hardy ")
TheDarkKnightRises.append("Joseph Gordon-Levitt")
TheDarkKnightRises.append("Anne Hathaway ")
ManOfSteel = LinkedList()
ManOfSteel.append(" Henry Cavill ")
ManOfSteel.append("Amy Adams ")
ManOfSteel.append("Michael Shannon ")
ManOfSteel.append("Diane Lane ")
ManOfSteel.append("Russell Crowe ")
ManOfSteel.append("Antje Traue ")
TheInception = LinkedList()
TheInception.append("Leonardo DiCaprio ")
TheInception.append("Joseph Gordon-Levitt ")
TheInception.append("Ellen Page ")
TheInception.append("Tom Hardy ")
TheInception.append("Ken Watanabe ")
TheInception.append("Dileep Rao ")
ShutterIsland = LinkedList()
ShutterIsland.append("Leonardo DiCaprio ")
ShutterIsland.append("Mark Ruffalo ")
ShutterIsland.append(" Ben Kingsley ")
ShutterIsland.append("Max von Sydow ")
ShutterIsland.append("Michelle Williams ")
TheGodFather = LinkedList()
TheGodFather.append("Marlon Brando ")
TheGodFather.append("Al Pacino ")
TheGodFather.append("James Caan ")
TheGodFather.append("Richard S. Castellano ")
TheGodFather.append("Robert Duvall ")
Ironman = LinkedList()
Ironman.append("Robert Downey Jr. ")
Ironman.append("Terrence Howard ")
Ironman.append("Jeff Bridges ")
Ironman.append("Gwyneth Paltrow ")
Ironman.append("Faran Tahir ")
Ironman.append("Leslie Bibb ")
Ironman.append("Shaun Toub ")
Conjuring = LinkedList()
Conjuring.append("Vera Farmiga ")
Conjuring.append("Patrick Wilson ")
Conjuring.append("Lili Taylor ")
Conjuring.append("Ron Livingston")
Conjuring.append("Shanley Caswell ")
CaptianAmericaWinterSolider = LinkedList()
CaptianAmericaWinterSolider.append("Chris Evans ")
CaptianAmericaWinterSolider.append("Samuel L. Jackson ")
CaptianAmericaWinterSolider.append("Scarlett Johansson ")
CaptianAmericaWinterSolider.append("Robert Redford ")
CaptianAmericaWinterSolider.append("SABESTAN STAND")
Predator = LinkedList()
Predator.append("Arnold Schwarzenegger ")
Predator.append("Carl Weathers ")
Predator.append("Elpidia Carrillo ")
Predator.append("Bill Duke ")
Predator.append("Jesse Ventura ")
Taken = LinkedList()
Taken.append("Liam Neeson ")
Taken.append("Leland Orser ")
Taken.append("Jon Gries ")
Taken.append("David Warshofsky ")
Taken.append("Holly Valance ")
BadBoys3 = LinkedList()
BadBoys3.append("Will Smith ")
BadBoys3.append("Martin Lawrence ")
BadBoys3.append("Vanessa Hudgens ")
BadBoys3.append("Alexander Ludwig ")
BadBoys3.append("Charles Melton ")
AvengersInfinityWar = LinkedList()
AvengersInfinityWar.append("Robert Downey Jr. ")
AvengersInfinityWar.append("Chris Hemsworth ")
AvengersInfinityWar.append(" Mark Ruffalo ")
AvengersInfinityWar.append("Chris Evans")
AvengersInfinityWar.append("Scarlett Johansson ")
FastAndFurios8 = LinkedList()
FastAndFurios8.append("Vin Diesel ")
FastAndFurios8.append("Jason Statham ")
FastAndFurios8.append("Dwayne Johnson ")
FastAndFurios8.append("Michelle Rodriguez ")
ShapeOfWater = LinkedList()
ShapeOfWater.append("Sally Hawkins ")
ShapeOfWater.append("Michael Shannon ")
ShapeOfWater.append("Richard Jenkins ")
ShapeOfWater.append("Octavia Spencer ")
ShapeOfWater.append("Michael Stuhlbarg")
Babylyon = LinkedList()
Babylyon.append("Margo Martindale ")
Babylyon.append("Riki Lindhome ")
Babylyon.append("Benito Martinez ")
Babylyon.append("Bruce MacVittie ")
Babylyon.append("David Powledge ")
Babylyon.append("Joe D'Angerio ")
TheShining = LinkedList()
TheShining.append("Steve Blum ")
TheShining.append("Brianne Brozey ")
TheShining.append("Melissa Fahn ")
TheShining.append("Barbara Goodson ")
TheShining.append("Steve Kramer ")
TheSixthSense = LinkedList()
TheSixthSense.append("Bruce Willis ")
TheSixthSense.append("Haley Joel Osment ")
TheSixthSense.append("Toni Collette ")
TheSixthSense.append("Trevor Morgan ")
TheSixthSense.append("Peter Anthony Tambakis ")
ShawasankRedemtion = LinkedList()
ShawasankRedemtion.append("Tim Robbins ")
ShawasankRedemtion.append("Morgan Freeman ")
ShawasankRedemtion.append("Bob Gunton ")
ShawasankRedemtion.append("William Sadler ")
ShawasankRedemtion.append("Clancy Brown ")
Rocky = LinkedList()
Rocky.append("Sylvester Stallone ")
Rocky.append("Talia Shire ")
Rocky.append("Burt Young ")
Rocky.append("Carl Weathers ")
Driver = LinkedList()
Driver.append("Ryan O'Neal ")
Driver.append("Bruce Dern ")
Driver.append("Isabelle Adjani ")
Driver.append("Ronee Blakley ")
JusticeLeague = LinkedList()
JusticeLeague.append("Ben Affleck ")
JusticeLeague.append("Henry Cavill ")
JusticeLeague.append("Amy Adams ")
JusticeLeague.append("Gal Gadot ")
JusticeLeague.append("Ezra Miller ")
Departed = LinkedList()
Departed.append("Leonardo DiCaprio ")
Departed.append("Matt Damon ")
Departed.append("Jack Nicholson ")
Departed.append("Mark Wahlberg ")
Departed.append("Martin Sheen ")
Departed.append("Ray Winstone ")
Parasite = LinkedList()
Parasite.append(" Kang-ho Song ")
Parasite.append("Sun-kyun Lee ")
Parasite.append("Yeo-jeong Jo ")
Parasite.append("Woo-sik Choi ")
Parasite.append(" So-dam Park ")
ToyStory = LinkedList()
ToyStory.append("Tom Hanks ")
ToyStory.append("Tim Allen ")
ToyStory.append("Don Rickles ")
ToyStory.append(" Jim Varney ")
ToyStory.append("Wallace Shawn ")
SchindlerList = LinkedList()
SchindlerList.append("Liam Neeson")
SchindlerList.append("Ben Kingsley")
SchindlerList.append("Ralph Fiennes")
SchindlerList.append("Embeth Davidtz")
SchindlerList.append("Jonathan Sagall")
PulpFiction = LinkedList()
PulpFiction.append("John Travolta")
PulpFiction.append("Samuel L. Jackson")
PulpFiction.append("Uma Thurman")
PulpFiction.append("Harvey Keitel")
PulpFiction.append("Tim Roth")
FightClub = LinkedList()
FightClub.append("Brad Pitt")
FightClub.append("Edward Norton")
FightClub.append("Helena Bonham Carter")
FightClub.append("Meat Loaf Aday")
FightClub.append("Jared Leto")
FightClub.append("James Haygood")
Joker = LinkedList()
Joker.append("Joaquin Phoenix")
Joker.append("Robert De Niro")
Joker.append("Zazie Beetz")
Joker.append("Frances Conroy")
Joker.append("Glenn Fleshler")
ForrestGump = LinkedList()
ForrestGump.append("Tom Hanks")
ForrestGump.append(" Robin Wright")
ForrestGump.append("Gary Sinise")
ForrestGump.append("Mykelti Williamson ")
ForrestGump.append("Sally Field")
TheMatrix = LinkedList()
TheMatrix.append("Keanu Reeves")
TheMatrix.append("Laurence Fishburne")
TheMatrix.append("Carrie-Anne Moss")
TheMatrix.append("Hugo Weaving")
TheMatrix.append("Joe Pantoliano")
TheMatrix.append("Jhon Davis")
Goodfellas = LinkedList()
Goodfellas.append(" Robert De Niro")
Goodfellas.append("Ray Liotta")
Goodfellas.append("Joe Pesci")
Goodfellas.append("Lorraine Bracco")
Goodfellas.append("Paul Sorvino")
SevenSamurai = LinkedList()
SevenSamurai.append("Toshiro Mifune")
SevenSamurai.append("Takashi Shimura")
SevenSamurai.append("Keiko Tsushima")
SevenSamurai.append("Isao Kimura")
SevenSamurai.append("Daisuke Katō")
Seven = LinkedList()
Seven.append("Brad Pitt")
Seven.append("Morgan Freeman")
Seven.append("Gwyneth Paltrow")
Seven.append("John C. McGinley")
Seven.append("David Fincher")
CityofGod = LinkedList()
CityofGod.append(" Alexandre Rodrigues")
CityofGod.append("Leandro Firmino da Hora")
CityofGod.append("Jonathan Haagensen")
CityofGod.append("Phellipe Haagensen")
CityofGod.append("Douglas Silva")
LifeIsBeautiful = LinkedList()
LifeIsBeautiful.append("Roberto Benigni ")
LifeIsBeautiful.append("Nicoletta Braschi")
LifeIsBeautiful.append("Giorgio Cantarini")
LifeIsBeautiful.append("Giustino Durano")
LifeIsBeautiful.append("Horst Buchholz ")
SpiritedAway = LinkedList()
SpiritedAway.append("Rumi Hiiragi")
SpiritedAway.append("Miyu Irino")
SpiritedAway.append("Mari Natsuki")
SpiritedAway.append("Bunta Sugawara")
SpiritedAway.append("Horsti")

Streetfighter = LinkedList()
Streetfighter.append("Jean-Claude Van Damme")
Streetfighter.append("Raul Julia")
Streetfighter.append("Ming-Na Wen ")
Streetfighter.append("Damian Chapa")
Streetfighter.append("Kylie Minogue ")

TheGreenMile = LinkedList()
TheGreenMile.append(" Tom Hanks")
TheGreenMile.append("David Morse")
TheGreenMile.append("Bonnie Hunt")
TheGreenMile.append("Michael Clarke Duncan")
TheGreenMile.append("James Cromwell")

HarryPotterandtheDeathlyHallowsPart2 = LinkedList()
HarryPotterandtheDeathlyHallowsPart2.append("Ralph Fiennes ")
HarryPotterandtheDeathlyHallowsPart2.append("Michael Gambon ")
HarryPotterandtheDeathlyHallowsPart2.append("Alan Rickman ")
HarryPotterandtheDeathlyHallowsPart2.append("Daniel Radcliffe ")
HarryPotterandtheDeathlyHallowsPart2.append("Rupert Grint ")

Angelique = LinkedList()
Angelique.append("Michèle Mercier ")
Angelique.append("Robert Hossein ")
Angelique.append("Jean Rochefort ")
Angelique.append("Claude Giraud ")
Angelique.append("Giuliano Gemma ")

MeetJoeBlack = LinkedList()
MeetJoeBlack.append("Brad Pitt ")
MeetJoeBlack.append("Anthony Hopkins ")
MeetJoeBlack.append("Claire Forlani ")
MeetJoeBlack.append("Jake Weber ")
MeetJoeBlack.append("Marcia Gay Harden ")

TheNotebook = LinkedList()
TheNotebook.append("Tim Ivey ")
TheNotebook.append("Starletta DuPois ")
TheNotebook.append("Gena Rowlands ")
TheNotebook.append("James Garner ")
TheNotebook.append("Anthony-Michael Q. Thomas ")

QuantumofSolace = LinkedList()
QuantumofSolace.append("Daniel Craig ")
QuantumofSolace.append("Olga Kurylenko ")
QuantumofSolace.append("Mathieu Amalric ")
QuantumofSolace.append("Judi Dench ")
QuantumofSolace.append("Giancarlo Giannini ")

CocoBeforeChanel = LinkedList()
CocoBeforeChanel.append("Audrey Tautou ")
CocoBeforeChanel.append("Benoît Poelvoorde ")
CocoBeforeChanel.append("Alessandro Nivola ")
CocoBeforeChanel.append("Marie Gillain ")
CocoBeforeChanel.append("Emmanuelle Devos ")

MemoirsofaGeisha = LinkedList()
MemoirsofaGeisha.append("Suzuka Ohgo ")
MemoirsofaGeisha.append("Togo Igawa ")
MemoirsofaGeisha.append("Mako ")
MemoirsofaGeisha.append("Samantha Futerman ")
MemoirsofaGeisha.append("Elizabeth Sung ")

Armageddon = LinkedList()
Armageddon.append("Bruce Willis ")
Armageddon.append("Billy Bob Thornton ")
Armageddon.append("Ben Affleck ")
Armageddon.append("Liv Tyler ")
Armageddon.append("Will Patton ")

PiratesoftheCaribbeanAtWorldsEnd = LinkedList()
PiratesoftheCaribbeanAtWorldsEnd.append("Johnny Depp ")
PiratesoftheCaribbeanAtWorldsEnd.append("Geoffrey Rush ")
PiratesoftheCaribbeanAtWorldsEnd.append("Orlando Bloom ")
PiratesoftheCaribbeanAtWorldsEnd.append("Keira Knightley ")
PiratesoftheCaribbeanAtWorldsEnd.append(" Jack Davenport ")

CasinoRoyale = LinkedList()
CasinoRoyale.append("Daniel Craig ")
CasinoRoyale.append("Eva Green ")
CasinoRoyale.append("Mads Mikkelsen ")
CasinoRoyale.append(" Judi Dench ")
CasinoRoyale.append("Jeffrey Wright ")

Transformers = LinkedList()
Transformers.append("Shia LaBeouf ")
Transformers.append("Megan Fox ")
Transformers.append("Josh Duhamel ")
Transformers.append(" Tyrese Gibson ")
Transformers.append(" Rachael Taylor ")

BasicInstinct = LinkedList()
BasicInstinct.append("Michael Douglas ")
BasicInstinct.append("Sharon Stone ")
BasicInstinct.append("George Dzundza ")
BasicInstinct.append("Jeanne Tripplehorn ")
BasicInstinct.append("Denis Arndt ")

BeyondBorders = LinkedList()
BeyondBorders.append("Angelina Jolie ")
BeyondBorders.append("Clive Owen ")
BeyondBorders.append("Teri Polo ")
BeyondBorders.append("Linus Roache ")
BeyondBorders.append("Noah Emmerich ")

TheTwilightSagaBreakingDawnPart2 = LinkedList()
TheTwilightSagaBreakingDawnPart2.append("Kristen Stewart ")
TheTwilightSagaBreakingDawnPart2.append("Robert Pattinson ")
TheTwilightSagaBreakingDawnPart2.append("Taylor Lautner")
TheTwilightSagaBreakingDawnPart2.append("Peter Facinelli ")
TheTwilightSagaBreakingDawnPart2.append("Elizabeth Reaser ")

XMenTheLastStand = LinkedList()
XMenTheLastStand.append("Hugh Jackman ")
XMenTheLastStand.append("Halle Berry ")
XMenTheLastStand.append("Ian McKellen ")
XMenTheLastStand.append("Patrick Stewart ")
XMenTheLastStand.append("Famke Janssen ")

TheLordoftheRingsTheFellowshipoftheRing = LinkedList()
TheLordoftheRingsTheFellowshipoftheRing.append("Alan Howard ")
TheLordoftheRingsTheFellowshipoftheRing.append(" Noel Appleby ")
TheLordoftheRingsTheFellowshipoftheRing.append("Sean Astin ")
TheLordoftheRingsTheFellowshipoftheRing.append("Sala Baker ")
TheLordoftheRingsTheFellowshipoftheRing.append("Sean Bean ")

TheLordoftheRingsTheTwoTowers = LinkedList()
TheLordoftheRingsTheTwoTowers.append("Bruce Allpress ")
TheLordoftheRingsTheTwoTowers.append("Sean Astin ")
TheLordoftheRingsTheTwoTowers.append("John Bach ")
TheLordoftheRingsTheTwoTowers.append("Sala Baker ")
TheLordoftheRingsTheTwoTowers.append("Cate Blanchett ")

TheAvengers = LinkedList()
TheAvengers.append("Robert Downey Jr. ")
TheAvengers.append("Chris Evans ")
TheAvengers.append("Mark Ruffalo ")
TheAvengers.append("Chris Hemsworth ")
TheAvengers.append("Scarlett Johansson 	Scarlett Johansson ")

Shrek = LinkedList()
Shrek.append("Mike Myers ")
Shrek.append("Eddie Murphy ")
Shrek.append("Cameron Diaz ")
Shrek.append("John Lithgow ")
Shrek.append("Vincent Cassel ")

SpiderMan = LinkedList()
SpiderMan.append("Tobey Maguire ")
SpiderMan.append("Willem Dafoe ")
SpiderMan.append("Kirsten Dunst ")
SpiderMan.append("James Franco ")
SpiderMan.append("Cliff Robertson ")

TheBookofEli = LinkedList()
TheBookofEli.append("Denzel Washington ")
TheBookofEli.append("Gary Oldman ")
TheBookofEli.append("Mila Kunis ")
TheBookofEli.append("Ray Stevenson ")
TheBookofEli.append("Jennifer Beals")

IAmLegend = LinkedList()
IAmLegend.append("Will Smith ")
IAmLegend.append(" Alice Braga ")
IAmLegend.append("Charlie Tahan ")
IAmLegend.append("Salli Richardson-Whitfield ")
IAmLegend.append("Willow Smith ")

MinorityReport = LinkedList()
MinorityReport.append("Tom Cruise ")
MinorityReport.append("Max von Sydow ")
MinorityReport.append("Steve Harris ")
MinorityReport.append("Neal McDonough ")
MinorityReport.append("Patrick Kilpatrick ")

VanillaSky = LinkedList()
VanillaSky.append("Tom Cruise ")
VanillaSky.append("Penélope Cruz ")
VanillaSky.append("Cameron Diaz ")
VanillaSky.append("Cameron Diaz ")
VanillaSky.append("Jason Lee ")

Enough = LinkedList()
Enough.append("Jennifer Lopez ")
Enough.append("Billy Campbell ")
Enough.append("Tessa Allen ")
Enough.append("Juliette Lewis ")
Enough.append("Dan Futterman ")

InHerShoes = LinkedList()
InHerShoes.append("Cameron Diaz ")
InHerShoes.append("Anson Mount ")
InHerShoes.append("Toni Collette ")
InHerShoes.append("Richard Burgi ")
InHerShoes.append(" Candice Azzara ")

TheHoliday = LinkedList()
TheHoliday.append("Cameron Diaz ")
TheHoliday.append("Kate Winslet ")
TheHoliday.append("Jude Law ")
TheHoliday.append("Jack Black ")
TheHoliday.append("Eli Wallach ")

PearlHarbor = LinkedList()
PearlHarbor.append("Ben Affleck ")
PearlHarbor.append("Josh Hartnett ")
PearlHarbor.append("Kate Beckinsale ")
PearlHarbor.append("William Lee Scott ")
PearlHarbor.append("Greg Zola ")

HesJustNotThatIntoYou = LinkedList()
HesJustNotThatIntoYou.append("Morgan Lily" )
HesJustNotThatIntoYou.append("Trenton Rogers ")
HesJustNotThatIntoYou.append("Michelle Carmichael ")
HesJustNotThatIntoYou.append("Jasmine Woods ")
HesJustNotThatIntoYou.append("Sabrina Revelle ")

ABeautifulMind = LinkedList()
ABeautifulMind.append("Russell Crowe ")
ABeautifulMind.append("Ed Harris ")
ABeautifulMind.append("Jennifer Connelly ")
ABeautifulMind.append("Christopher Plummer ")
ABeautifulMind.append("Paul Bettany ")

CinemaParadiso = LinkedList()
CinemaParadiso.append("Vince Vaughn ")
CinemaParadiso.append("Jennifer Aniston ")
CinemaParadiso.append("Joey Lauren Adams ")
CinemaParadiso.append("Cole Hauser ")
CinemaParadiso.append("Jon Favreau ")

TheBreakUp = LinkedList()
TheBreakUp.append("Vince Vaughn ")
TheBreakUp.append("Jennifer Aniston ")
TheBreakUp.append("Joey Lauren Adams ")
TheBreakUp.append("Cole Hauser ")
TheBreakUp.append("Jon Favreau ")

DearJohn = LinkedList()
DearJohn.append("Channing Tatum ")
DearJohn.append("Amanda Seyfried ")
DearJohn.append("Richard Jenkins ")
DearJohn.append("Henry Thomas ")
DearJohn.append("D.J. Cotrona ")

IronMan3 = LinkedList()
IronMan3.append("Robert Downey Jr. ")
IronMan3.append("Gwyneth Paltrow ")
IronMan3.append("Don Cheadle ")
IronMan3.append("Guy Pearce ")
IronMan3.append("Rebecca Hall ")

ApocalypseNow = LinkedList()
ApocalypseNow.append("Marlon Brando ")
ApocalypseNow.append("Martin Sheen ")
ApocalypseNow.append(" Robert Duvall ")
ApocalypseNow.append("Frederic Forrest ")
ApocalypseNow.append("Sam Bottoms ")

Memento = LinkedList()
Memento.append("Guy Pearce ")
Memento.append("Carrie-Anne Moss ")
Memento.append("Joe Pantoliano ")
Memento.append("Mark Boone Junior ")
Memento.append("Russ Fega ")

JhonWick = LinkedList()
JhonWick.append("Keanu Reeves ")
JhonWick.append("Michael Nyqvist ")
JhonWick.append("Alfie Allen ")
JhonWick.append("Willem Dafoe ")

TransformersDarkKnight = LinkedList()
TransformersDarkKnight.append("Shia LaBeouf ")
TransformersDarkKnight.append("Megan Fox ")
TransformersDarkKnight.append("Josh Duhamel ")
TransformersDarkKnight.append("Tyrese Gibson ")

Rituals = LinkedList()
Rituals.append("Hal Holbrook ")
Rituals.append("Lawrence Dane ")
Rituals.append("Robin Gammell ")
Rituals.append("Ken James ")

Looper = LinkedList()
Looper.append("Joseph Gordon-Levitt ")
Looper.append("Bruce Willis ")
Looper.append("Emily Blunt ")
Looper.append("Paul Dano ")
Looper.append(" Noah Segan ")

JurassicPark = LinkedList()
JurassicPark.append("Sam Neill ")
JurassicPark.append("Laura Dern ")
JurassicPark.append("Jeff Goldblum ")
JurassicPark.append("Richard Attenborough ")

BlackPanther = LinkedList()
BlackPanther.append("Chadwick Boseman ")
BlackPanther.append("Michael B. Jordan ")
BlackPanther.append("Lupita Nyong'o ")
BlackPanther.append("Danai Gurira ")

Gladiator = LinkedList()
Gladiator.append("Russell Crowe ")
Gladiator.append("Joaquin Phoenix ")
Gladiator.append("Connie Nielsen ")
Gladiator.append("Oliver Reed ")

Extraction = LinkedList()
Extraction.append("Chris Hemsworth ")
Extraction.append("Bryon Lerum ")
Extraction.append("Ryder Lerum ")
Extraction.append("Rudhraksh Jaiswal ")

Skyfall = LinkedList()
Skyfall.append("Daniel Craig ")
Skyfall.append("Judi Dench ")
Skyfall.append("Javier Bardem ")
Skyfall.append("Ralph Fiennes ")

NightCrawler = LinkedList()
NightCrawler.append("Eryn Brooke ")
NightCrawler.append("Joel Ferrell ")
NightCrawler.append("Joey Greco ")
NightCrawler.append("Mathew Greer ")

SourceCode = LinkedList()
SourceCode.append("Jake Gyllenhaal ")
SourceCode.append("Michelle Monaghan ")
SourceCode.append("Vera Farmiga ")
SourceCode.append("Jeffrey Wright ")

NonStop = LinkedList()
NonStop.append("Liam Neeson ")
NonStop.append("Julianne Moore ")
NonStop.append("Scoot McNairy ")
NonStop.append("Michelle Dockery ")

bst.insert("2018", "Ip Man", "2:2:40", "PG-17", IpMan)
bst.insert("2016", "Finding nemo", "3:40:02", "PG-17", Findingnemo)
bst.insert("2020", "Killer", "1:54:10", "G", Killer)
bst.insert("2018", "Alien", "2:30:40", "G", Alien)
bst.insert("2018", "American Sniper", "2:30:40", "G", AmericanSniper)
bst.insert("2021", "Terminator", "3:2:40", "R", Terminator)
bst.insert("2018", "Jaws-3", "2:21:40", "PG-12", Jaws3)
bst.insert("2001", "Fast And Furios", "3:2:40", "PG-17", FastAndFurios)
bst.insert("2013", "The Internship", "3:2:40", "N-R", TheInternship)
bst.insert("2017", "Baby Driver", "3:12:10", "PG", BabyDriver)
bst.insert("2015", "Mission-Impossible", "2:22:50", "G", MissionImpossible)
bst.insert("2012", "Bird Box", "1:34:40", "R", BirdBox)
bst.insert("2008", "Million Dollar Baby", "1:32:10", "PG-16", MillionDollarBaby)
bst.insert("2016", "IpMan-3", "3:12:40", "G", IpMan3)
bst.insert("2010", "The Dark Knight Rises", "1:42:10", "PG-12", TheDarkKnightRises)
bst.insert("2011", "Man Of Steel", "3:45:40", "PG-12", ManOfSteel)
bst.insert("2018", "The Inception", "3:15:23", "G", TheInception)
bst.insert("2010", "Shutter Island", "3:5:44", "R", ShutterIsland)
bst.insert("1973", "The God Father", "1:12:45", "PG-12", TheGodFather)
bst.insert("2009", "Iron man", "2:34:10", "NR", Ironman)
bst.insert("2016", "Conjuring", "3:10:22", "PG-18", Conjuring)
bst.insert("2020", "Captian America Winter Solider", "2:54:10", "G", CaptianAmericaWinterSolider)
bst.insert("2017", "Predator", "1:45:30", "G", Predator)
bst.insert("2011", "Taken", "3:10:10", "NR", Taken)
bst.insert("2020", "Bad Boys-3", "2:12:30", "R", BadBoys3)
bst.insert("2018", "Avengers Infinity War", "2:21:40", "PG-12", AvengersInfinityWar)
bst.insert("2014", "Fast And Furios-8", "3:42:12", "G", FastAndFurios8)
bst.insert("2013", "Shape Of Water", "3:42:50", "NR", ShapeOfWater)
bst.insert("2017", "Baby lyon", "2:22:10", "PG", Babylyon)
bst.insert("1969", "The Shining", "2:22:50", "PG-16", TheShining)
bst.insert("1996", "The Sixth Sense", "3:14:40", "R", TheSixthSense)
bst.insert("1994", "Shawasank Redemtion", "2:52:50", "PG-18", ShawasankRedemtion)
bst.insert("1973", "Rocky", "3:41:10", "NR", Rocky)
bst.insert("2011", "Driver", "1:54:12", "PG-12", Driver)
bst.insert("2015", "Justice League", "3:15:20", "PG", JusticeLeague)
bst.insert("2018", "Departed", "3:15:23", "G", Departed)
bst.insert("2019", "Parasite", "3:5:44", "R", Parasite)
bst.insert("1995", "Toy Story", "3:2:45", "NR", ToyStory)
bst.insert("1993", "Schindler List", "3:2:45", "NR", SchindlerList)
bst.insert("1999", "Pulp Fiction", "3:2:15", "PG-18", PulpFiction)
bst.insert("1995", "Seven", "3:2:45", "PG-18", Seven)
bst.insert("1954", "Seven Samurai", "3:2:25", "G", SevenSamurai)
bst.insert("2001", "Spirited Away", "3:2:35", "PG", SpiritedAway)
bst.insert("1991", "Life Is Beautiful", "2:2:45", "G", LifeIsBeautiful)
bst.insert("1999", "The Green Mile", "3:2:25", "PG-18", TheGreenMile)
bst.insert("1996", "The Matrix", "3:2:35", "PG-12", TheMatrix)
bst.insert("2019", "Joker", "2:12:15", "PG-17", Joker)
bst.insert("1989", "Good fellas", "3:32:10", "NR", Goodfellas)
bst.insert("1995", "Forrest Gump", "2:22:12", "PG-12", ForrestGump)
bst.insert("1986", "City Of God", "3:25:45", "G", CityofGod)
bst.insert("1999", "Fight Club", "2:21:45", "PG-16", FightClub)
bst.insert("2015", "Street Fighter", "2:10:45", "PG", Streetfighter)
bst.insert("2011", "Harry Porter Deathly Hallows", "3:50:4", "PG-12", HarryPotterandtheDeathlyHallowsPart2)
bst.insert("2002", "Angelique", "3:21:45", "R", Angelique)
bst.insert("2004", "Meet Joe Black", "2:2:45", "R", MeetJoeBlack)
bst.insert("2005", "The Notebook", "4:2:45", "PG-17", TheNotebook)
bst.insert("2006", "Quantom Of Solace", "1:42:45", "PG", QuantumofSolace)
bst.insert("2007", "Coco Before Chanel", "2:22:15", "NR", CocoBeforeChanel)
bst.insert("1965", "Memoirs Of AGeisha", "2:21:45", "G", MemoirsofaGeisha)
bst.insert("1979", "Armageddon", "2:12:55", "G", Armageddon)
bst.insert("2008", "Pirates Of The Caribbean At Worlds End", "", "PG", PiratesoftheCaribbeanAtWorldsEnd)
bst.insert("2014", "Casino Royale", "2:21:10", "PG-12", CasinoRoyale)
bst.insert("2010", "Transformers", "3:22:45", "PG", Transformers)
bst.insert("1999", "Basic Instinct", "1:33:33", "NR", BasicInstinct)
bst.insert("2002", "Beyond Borders", "2:22:12", "NR", BeyondBorders)
bst.insert("2009", "The Twilight Saga Breaking Dawn Part2", "3:31:52", "NR", TheTwilightSagaBreakingDawnPart2)
bst.insert("2008", "XMen The Last Stand", "2:21:25", "PG-12", XMenTheLastStand)
bst.insert("2007", "The Lord of the Rings The Fellowship Of The Ring", "2:22:45", "R",
           TheLordoftheRingsTheFellowshipoftheRing)
bst.insert("2001", "The Lord Of The Rings The Two Towers)", "1:45:32", "G", TheLordoftheRingsTheTwoTowers)
bst.insert("2012", "The Avengers", "3:45:23", "PG-16", TheAvengers)
bst.insert("2012", "Shrek", "1:20:25", "PG", Shrek)
bst.insert("2006", "SpiderMan", "2:34:41", "G", SpiderMan)
bst.insert("2009", "The Book Of Eli", "3:03:22", "R", TheBookofEli)
bst.insert("2001", "Iam Legend", "3:21:45", "PG-12", IAmLegend)
bst.insert("2001", "Minority Report", "3:2:45", "PG-16", MinorityReport)
bst.insert("1998", " Vanilla Sky", "3:21:30", "PG", VanillaSky)
bst.insert("1993", "Enough", "1:21:45", "G", Enough)
bst.insert("1991", "In Her Shoes", "2:21:21", "G", InHerShoes)
bst.insert("1999", "The Holiday", "3:21:15", "NR", TheHoliday)
bst.insert("2009", "Pearl Harbor ", "2:21:45", "NR", PearlHarbor)
bst.insert("2007", "He Just Not That Into You", "2:21:45", "NR", HesJustNotThatIntoYou)
bst.insert("2007", "A Beautiful Mind", "3:42:45", "R", ABeautifulMind)
bst.insert("2005", "Cinema Paradiso", "2:12:25", "PG", CinemaParadiso)
bst.insert("2006", "The BreakUp", "1:29:40", "PG-17", TheBreakUp)
bst.insert("2009", "Dear John", "2:27:45", "NR", DearJohn)
bst.insert("2012", "IronMan 3", "1:43:15", "R", IronMan3)
bst.insert("2015", "Apocalypse Now", "1:38:37", "NR", ApocalypseNow)
bst.insert("2015", "Jhon Wick", "3:58:12", "PG-18", JhonWick)
bst.insert("1993", "Jurassic Park", "2:44:02", "PG", JurassicPark)
bst.insert("2014", "Looper", "2:14:20", "PG-18", Looper)
bst.insert("2012", "Skyfall", "2:23:12", "R", Skyfall)
bst.insert("2020", "Extraction", "3:24:43", "NR", Extraction)
bst.insert("2018", "Black Panther", "2:45:52", "PG", BlackPanther)
bst.insert("2014", "Night Crawler", "2:48:8", "G", NightCrawler)
bst.insert("2011", "Source Code", "2:13:18", "PG", SourceCode)
bst.insert("2017", "Rituals", "3:52:02", "NR", Rituals)
bst.insert("2017", "Transformers Dark Knight", "2:12:20", "PG-12", TransformersDarkKnight)
bst.insert("2004", "Gladiator", "2:19:10", "PG-18", Gladiator)
bst.insert("2004", "Memento", "2:41:20", "G", Memento)
bst.insert("2014", "Non Stop", "3:41:20", "PG-12", NonStop)

while (True):
    print("-------------------------Welcome To Movie Storage Application-------------------------------------")
    print()
    print(" 1 : To Insert A movie ")
    print(" 2 : To Search A Movie by Title ")
    print(" 3 : To Show All The Movies   ")
    print(" 4 : To Edit Cast OF The Movie")
    print(" 5: To Search Movies By Year  ")
    print(" 6: To Search Movies By Ratings ")
    print("7: To See Total Numbers Of Movies ")
    print("8: To See Total Numbers Of Movies Between Given Years ")
    print("9: To The Delete The Movie From BST Storage")
    print("10: To The View The Movie Trailer Stored In BST Storage")

    print("11: To Exit")
    choice = int(input("Enter your Choice: "))

    if (choice == 11):
        break
    if (choice == 9):
        print("Please Enter The MOvie Name To Delete It")
        movie = input()
        bst.deleteNode(movie)
    if (choice == 1):
        print("please Tell the Movie Title")
        title = input()
        print("please Mention the Movie Realese Year")
        year = input()
        print("please Tell the Duration Of The Movie")
        Duration = input()
        print("please Tell the Rating Of The Movie ")
        Raing = input()
        cast = "Yes"
        temp = cast
        temp = title
        cast = temp
        cast = LinkedList()
        arr = []
        n = int(input("Tell How Many Cast Memebers Are There : "))

        print("\n")
        for i in range(0, n):
            print("Please Enter The Name Cast Member", [i + 1], ":")
            item = input()
            arr.append(item)
        for i in arr:
            cast.append(i)
        print(bst.insert(year, title, Duration, Raing, cast))

    if (choice == 2):
        print("please Tell the Movie Title")
        title2 = input()
        bst.find(title2)
        print('\n')

    if (choice == 3):
        bst.inorder_print_tree()

    if (choice == 4):
        print("Enter Movie Name To edit it's Cast")
        movie = input()
        if (movie == "FastAndFurios"):
            movie = FastAndFurios
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Terminator"):
            movie = Terminator
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Fast And Furious 8"):
            movie = FastAndFurios8
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Dark Knight Rises"):
            movie = TheDarkKnightRises
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The God Father"):
            movie = TheGodFather
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Incception"):
            movie = TheInception
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Internship"):
            movie = TheInternship
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Shining"):
            movie = TheShining
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Sixth Sense"):
            movie = TheSixthSense
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Alien"):
            movie = Alien
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "AMerican Sniper"):
            movie = AmericanSniper
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Baby Driver"):
            movie = BabyDriver
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "baby Lyon"):
            movie = Babylyon
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Bad Boys 3"):
            movie = BadBoys3
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Conjuring"):
            movie = Conjuring
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Departed"):
            movie = Departed
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Driver"):
            movie = Driver
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Finding Nemo"):
            movie = Findingnemo
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Jaws 3"):
            movie = Jaws3
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Justice League"):
            movie = JusticeLeague
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Killer"):
            movie = Killer
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Million Dollar Baby"):
            movie = MillionDollarBaby
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Mission Impossible "):
            movie = MissionImpossible
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Rocky"):
            movie = Rocky
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Shape Of Water"):
            movie = ShapeOfWater
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Shawasank Redemption"):
            movie = ShawasankRedemtion
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Shutter island"):
            movie = ShutterIsland
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Taken"):
            movie = Taken
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Toy Story"):
            movie = ToyStory
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Bird Box"):
            movie = BirdBox
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Good Fellas"):
            movie = Goodfellas
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Seven Samurai"):
            movie = SevenSamurai
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Seven"):
            movie = Seven
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Matrix"):
            movie = TheMatrix
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Green Mile"):
            movie = TheGreenMile
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Spirited Away"):
            movie = SpiritedAway
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Life Is Beautiful"):
            movie = LifeIsBeautiful
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "City Of God"):
            movie = CityofGod
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Pulp Fiction"):
            movie = PulpFiction
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Fight Club"):
            movie = FightClub
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Forrest Gump"):
            movie = ForrestGump
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Schindler List"):
            movie = SchindlerList
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Joker"):
            movie = Joker
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Non Stop"):
            movie = NonStop
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Night Crawler"):
            movie = NightCrawler
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Memento"):
            movie = Memento
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()

        elif (movie == "Jhon Wick"):
            movie = JhonWick
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Transformers Dark Knight"):
            movie = TransformersDarkKnight
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Rituals"):
            movie = Rituals
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Looper"):
            movie = Looper
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Extraction"):
            movie = Extraction
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Angelique"):
            movie = Angelique
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "A Beautiful Mind"):
            movie = ABeautifulMind
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Apocalypse Now"):
            movie = ApocalypseNow
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Armageddon"):
            movie = Armageddon
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Basic Instinct"):
            movie = BasicInstinct
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Black Panther"):
            movie = BlackPanther
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Beyond Borders"):
            movie = BeyondBorders
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Casino Royale"):
            movie = CasinoRoyale
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Cinema Paradiso"):
            movie = CinemaParadiso
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Coco Before Chanel"):
            movie = CocoBeforeChanel
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Dear John"):
            movie = DearJohn
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "In Her Shoes"):
            movie = InHerShoes
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "IronMan 3"):
            movie = IronMan3
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Jurassic Park"):
            movie = JurassicPark
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Minority Report"):
            movie = MinorityReport
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Meet Joe Black"):
            movie = MeetJoeBlack
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Memoirs Of A Geisha"):
            movie = MemoirsofaGeisha
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Pearl Harbor"):
            movie = PearlHarbor
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Pirates Of The Caribbean At Worlds End"):
            movie = PiratesoftheCaribbeanAtWorldsEnd
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Quantum Of Solace"):
            movie = QuantumofSolace
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Shrek"):
            movie = Shrek
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Skyfall"):
            movie = Skyfall
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Source Code"):
            movie = SourceCode
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "SpiderMan"):
            movie = SpiderMan
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "TheAvengers"):
            movie = TheAvengers
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Book Of Eli"):
            movie = TheBookofEli
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The BreakUp"):
            movie = TheBreakUp
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Holiday"):
            movie = TheHoliday
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Lord Of The Rings The Fellowship Of The Ring"):
            movie = TheLordoftheRingsTheFellowshipoftheRing
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Lord Of The Rings The Two Towers"):
            movie = TheLordoftheRingsTheTwoTowers
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Notebook"):
            movie = TheNotebook
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "The Twilight Saga Breaking Dawn Part2"):
            movie = TheTwilightSagaBreakingDawnPart2
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "Vanilla Sky"):
            movie = VanillaSky
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()
        elif (movie == "XMen The Last Stand"):
            movie = XMenTheLastStand
            print("The Cast Of The Movie IS:")
            movie.print_list()
            print("Please Enter Delete To Delete Member From The Cast Or Enter Add To Add Another Cast Member")
            option = input()
            if (option == "Add"):
                print("Enter The Memeber Name To Add It In The Cast")
                actor = input()
                movie.append(actor)
                movie.print_list()
            elif (option == "Delete"):
                print("Enter The Memeber Name To Delete It From The Cast")
                actor = input()
                movie.deleteNode(actor)
                movie.print_list()

        else:
            print("Movie Not Availible")

    if (choice == 5):
        year = input(print("Please Tell the Movie Release Year"))
        bst.year(year)
        print(" ")
        bst.dbl3.head = bst.dbl3.mergeSort(bst.dbl3.head)
        print(" ")
        print("SORTED DOUBLY LINKED LIST OF MOVIES")
        print(" ")
        bst.dbl3.printList(bst.dbl3.head)
        print('\n')

    if (choice == 6):
        print("Please Tell the Movie  Ratings")
        ratings = input()
        bst.ratings(ratings)
        print(" ")
        bst.dbl2.head = bst.dbl2.mergeSort(bst.dbl2.head)
        print(" ")
        print("SORTED DOUBLY LINKED LIST OF MOVIES")
        print(" ")
        bst.dbl2.printList(bst.dbl2.head)
        print('\n')

    if (choice == 7):
        print("Total Number Of Movies Availible")
        print(bst.size())
        print('\n')
    if (choice == 8):
        print("Please Enter The Starting year")
        Initial = input()
        print("Please Enter The Ending year")
        Final = input()
        print(f"Total Number Of Movies Between", Initial, "To", Final)
        print(bst.duoyear(Initial, Final))
        print(" ")
        bst.dbl.head = bst.dbl.mergeSort(bst.dbl.head)
        print(" ")
        print("SORTED DOUBLY LINKED LIST OF MOVIES")
        print(" ")
        bst.dbl.printList(bst.dbl.head)
        print('\n')
    if (choice == 10):
        print("Please Enter Movie Name To View its Trailers")
        url = input()
        if (url == "Fast And Furios"):
            url = arrFastAndFurios
            print("The Cast Of The Movie IS:")

        elif (url == "Terminator"):
            url = arrTerminator

        elif (url == "Fast And Furious 8"):
            url = arrFastAndFurios8

        elif (url == "The Dark Knight Rises"):
            url = arrTheDarkKnightRises

        elif (url == "The God Father"):
            url = arrTheGodFather

        elif (url == "The Incception"):
            url = arrTheInception

        elif (url == "The Internship"):
            url = arrTheInternship

        elif (url == "The Shining"):
            url = arrTheShining

        elif (url == "The Sixth Sense"):
            url = arrTheSixthSense

        elif (url == "Alien"):
            url = arrAlien

        elif (url == "AMerican Sniper"):
            url = arrAmericanSniper

        elif (url == "Baby Driver"):
            url = arrBabyDriver

        elif (url == "baby Lyon"):
            url = arrBabylyon

        elif (url == "Bad Boys 3"):
            url = arrBadBoys3

        elif (url == "The Conjuring"):
            url = arrConjuring

        elif (url == "Departed"):
            url = arrDeparted

        elif (url == "Driver"):
            url = arrDriver

        elif (url == "Finding Nemo"):
            url = arrFindingnemo

        elif (url == "Jaws 3"):
            url = arrJaws3

        elif (url == "Justice League"):
            url = arrJusticeLeague

        elif (url == "Killer"):
            url = arrKiller

        elif (url == "Million Dollar Baby"):
            url = arrMillionDollarBaby

        elif (url == "Mission Impossible "):
            url = arrMissionImpossible

        elif (url == "Rocky"):
            url = arrRocky

        elif (url == "Shape Of Water"):
            url = arrShapeOfWater

        elif (url == "Shawasank Redemption"):
            url = arrShawasankRedemtion

        elif (url == "Shutter island"):
            url = arrShutterIsland

        elif (url == "Taken"):
            url = arrTaken

        elif (url == "Toy Story"):
            url = arrToyStory

        elif (url == "Bird Box"):
            url = arrBirdBox

        elif (url == "Good Fellas"):
            url = arrGoodfellas

        elif (url == "Seven Samurai"):
            url = arrSevenSamurai

        elif (url == "Seven"):
            url = arrSeven

        elif (url == "The Matrix"):
            url = arrTheMatrix

        elif (url == "The Green Mile"):
            url = arrTheGreenMile

        elif (url == "Spirited Away"):
            url = arrSpiritedAway

        elif (url == "Life Is Beautiful"):
            url = arrLifeIsBeautiful

        elif (url == "City Of God"):
            url = arrCityofGod

        elif (url == "Pulp Fiction"):
            url = arrPulpFiction

        elif (url == "Fight Club"):
            url = arrFightClub

        elif (url == "Forrest Gump"):
            url = arrForrestGump

        elif (url == "Schindler List"):
            url = arrSchindlerList

        elif (url == "Joker"):
            url = arrJoker

        elif (url == "Non Stop"):
            url = arrNonStop

        elif (url == "Night Crawler"):
            url = arrNightCrawler

        elif (url == "Memento"):
            url = arrMemento


        elif (url == "Jhon Wick"):
            url = arrJhonWick

        elif (url == "Transformers Dark Knight"):
            url = arrTransformersDarkKnight

        elif (url == "Rituals"):
            url = arrRituals

        elif (url == "Looper"):
            url = arrLooper

        elif (url == "Extraction"):
            url = arrExtraction

        elif (url == "Angelique"):
            url = arrAngelique

        elif (url == "A Beautiful Mind"):
            url = arrABeautifulMind

        elif (url == "Apocalypse Now"):
            url = arrApocalypseNow

        elif (url == "Armageddon"):
            url = arrArmageddon

        elif (url == "Basic Instinct"):
            url = arrBasicInstinct

        elif (url == "Black Panther"):
            url = arrBlackPanther

        elif (url == "Beyond Borders"):
            url = arrBeyondBorders

        elif (url == "Casino Royale"):
            url = arrCasinoRoyale

        elif (url == "Cinema Paradiso"):
            url = arrCinemaParadiso

        elif (url == "Coco Before Chanel"):
            url = arrCocoBeforeChanel

        elif (url == "Dear John"):
            url = arrDearJohn

        elif (url == "In Her Shoes"):
            url = arrInHerShoes

        elif (url == "IronMan 3"):
            url = arrIronMan3

        elif (url == "Jurassic Park"):
            url = arrJurassicPark

        elif (url == "Minority Report"):
            url = arrMinorityReport

        elif (url == "Meet Joe Black"):
            url = arrMeetJoeBlack

        elif (url == "Memoirs Of A Geisha"):
            url = arrMemoirsofaGeisha

        elif (url == "Pearl Harbor"):
            url = arrPearlHarbor

        elif (url == "Pirates Of The Caribbean At Worlds End"):
            url = arrPiratesoftheCaribbeanAtWorldsEnd

        elif (url == "Quantum Of Solace"):
            url = arrQuantumofSolace

        elif (url == "Shrek"):
            url = arrShrek

        elif (url == "Skyfall"):
            url = arrSkyfall

        elif (url == "Source Code"):
            url = arrSourceCode

        elif (url == "SpiderMan"):
            url = arrSpiderMan

        elif (url == "TheAvengers"):
            url = arrTheAvengers

        elif (url == "The Book Of Eli"):
            url = arrTheBookofEli

        elif (url == "The BreakUp"):
            url = arrTheBreakUp

        elif (url == "The Holiday"):
            url = arrTheHoliday

        elif (url == "The Lord Of The Rings The Fellowship Of The Ring"):
            url = arrTheLordoftheRingsTheFellowshipoftheRing

        elif (url == "The Lord Of The Rings The Two Towers"):
            url = arrTheLordoftheRingsTheTwoTowers

        elif (url == "The Notebook"):
            url = arrTheNotebook

        elif (url == "The Twilight Saga Breaking Dawn Part2"):
            url = arrTheTwilightSagaBreakingDawnPart2

        elif (url == "Vanilla Sky"):
            url = arrVanillaSky

        elif (url == "XMen The Last Stand"):
            url = arrXMenTheLastStand


        else:
            print("Movie Not Availible")
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(playurl)
        media.get_mrl()
        player.set_media(media)
        player.play()
        time.sleep(600)
