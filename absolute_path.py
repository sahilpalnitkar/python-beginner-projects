# Given an absolute path for a file (Unix-style), simplify it. Or in other words, 
# convert it to the canonical path.

# In a UNIX-style file system, a period . refers to the current directory. Furthermore,
# a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

# Note that the returned canonical path must always begin with a slash /, and there must be only a 
# single slash / between two directory names. The last directory name (if it exists) must not end with a 
# trailing /. Also, the canonical path must be the shortest string representing the absolute path.



def main():
    def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """
        pathlist = [p for p in path.split('/') if p]
        stack = []
        for p in pathlist:
            if p == '..':
                if stack: stack.pop()
            elif p != '.':
                stack.append(p)
        print '/' + '/'.join(stack)
        return '/' + '/'.join(stack)

    simplifyPath("/home/test/a/b/../..//final/")

if __name__ == "__main__":
        main()           