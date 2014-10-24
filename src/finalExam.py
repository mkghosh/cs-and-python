'''
Final Exam coding section
'''

# p3-4
def bSort(lst):

    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])
        return unite(front, back)


# p5
class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))
 
    def setGrade(self, grade, course="6.01x"):
        """
       grade: integer greater than or equal to 0 and less than or equal to 100
       course: string
 
       This method sets the grade in the courseInfo object named by `course`.  
 
       If `course` was not part of the initialization, then no grade is set, and no
       error is thrown.
 
       The method does not return a value.
       """
        for c in self.myCourses:
            if c.courseName == course:
                c.setGrade( grade)
       
 
    def getGrade(self, course="6.02x"):
        """
       course: string
 
       This method gets the grade in the the courseInfo object named by `course`.
 
       returns: the integer grade for `course`.  
       If `course` was not part of the initialization, returns -1.
       """
        for c in self.myCourses:
            if c.courseName == course:
                return c.getGrade()
       
        return -1
 
    def setPset(self, pset, score, course="6.00x"):
        """
       pset: a string or a number
       score: an integer between 0 and 100
       course: string
 
       The `score` of the specified `pset` is set for the
       given `course` using the courseInfo object.
 
       If `course` is not part of the initialization, then no pset score is set,
       and no error is thrown.
       """
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName == course:
                self.myCourses[i].setPset( pset, score)
       
 
    def getPset(self, pset, course="6.00x"):
        """
       pset: a string or a number
       score: an integer between 0 and 100
       course: string        
 
       returns: The score of the specified `pset` of the given
       `course` using the courseInfo object.
       If `course` was not part of the initialization, returns -1.
       """
        for c in self.myCourses:
            if c.courseName == course:
                return c.getPset(pset)        
        return -1


# p6
class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent 
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common 
        ancestor as described in 5-2.

        degree removed is the distance to the common ancestor

        Keyword arguments: 
        a -- string that is the name of a
        b -- string that is the name of b
        """
        if a == b:
            return (-1,0)
        a = self.names_to_nodes[a]
        b = self.names_to_nodes[b]
        if a.is_parent(b) or b.is_parent(a):
            return (-1,0)
        ParentA = a
        ParentB = b        
        glA = 0
        glB = 0
        removed = 0
        cType = -1
        while(ParentA.get_parent() != None):
            glA += 1
            ParentA = ParentA.get_parent()
        while(ParentB.get_parent() != None):
            glB += 1
            ParentB = ParentB.get_parent()

        if( glA > glB):
            removed = glA-glB
        if( glA < glB):
            removed = glB-glA
        ParentA=a
        ParentB=b
        if( glA > glB+1):
            for i in range(glA-glB-1):
                ParentA = ParentA.get_parent()
        elif(glB > glA+1):      #jezeli roznica ich pokrewienstwa jest wieksza od 1
            for i in range(glB-glA-1):
                ParentB = ParentB.get_parent()       #zmniejsz ja do 1
        elif(glA == glB):    #jezeli sa na tym samym poziomie
            ParentA = a.get_parent()     # zmien ten poziom
            cType = 0
        if(glA > glB):
            while ParentA.is_parent(ParentB)==False:
                ParentA = ParentA.get_parent()
                ParentB = ParentB.get_parent()
                cType += 1
            return (cType, removed)
        else:
            while ParentB.is_parent(ParentA) == False:
                ParentA = ParentA.get_parent()
                ParentB = ParentB.get_parent()
                cType += 1
            return (cType, removed)


# p7 doubly linked list
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name


def insert(atMe, newFrob):
    """
   atMe: a Frob that is part of a doubly linked list
   newFrob:  a Frob with no links 
   This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
   """
   
    #NewFrob comes before atMe.
    if newFrob.name < atMe.name:
        if atMe.before != None and atMe.before == newFrob.before:
            newFrob.after = atMe
            atMe.before = newFrob
            newFrob.before.after = newFrob
        elif atMe.before == None:
            atMe.before = newFrob
            newFrob.after = atMe
        else:
            newFrob.after = atMe
            insert(atMe.before, newFrob)
    #NewFrob comes after atMe.    
    elif newFrob.name > atMe.name:
        if atMe.after != None and atMe.after == newFrob.after:
            newFrob.before = atMe
            atMe.after = newFrob
            newFrob.after.before = newFrob
        elif atMe.after == None:
            atMe.after = newFrob
            newFrob.before = atMe
        else:
            newFrob.before = atMe
            insert(atMe.after, newFrob)
 
    #NewFrob has the same name as atMe.
    else:
        newFrob.after = atMe.after
        atMe.after = newFrob
        newFrob.before = atMe
        if newFrob.after != None:
            newFrob.after.before = newFrob


def findFront(start):
    """
  start: a Frob that is part of a doubly linked list
  returns: the Frob at the beginning of the linked list
  """
    if (start.getBefore()==None):
        return start
    else:
        return findFront(start.getBefore())
