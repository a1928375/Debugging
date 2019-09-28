# Debugging

(1) Debugging Environments:  Debugging is critical to making high-quality software. In this problem I have inserted a bug into our JavaScript interpreter and you will have to fix it. In particular, we will focus on function call expressions. Suppose our code for eval_exp(), evaluating JavaScript expressions, looks like this :

   def eval_exp(exp,env): 
           etype = exp[0] 
           if etype == "identifier":
                   vname = exp[1]
                   value = env_lookup(vname,env) 
                   if value == None: 
                           print "ERROR: unbound variable " + vname
                   else:
                           return value
           elif etype == "number":
                   return float(exp[1])
           elif etype == "string":
                   return exp[1] 
           elif etype == "true":
                   return True
           ...
           elif etype == "call": 
                   return eval_call(exp,env) 
                   
Then the function eval_call() is responsible for handling function call expressions. I have written a buggy version of it below. You must find and fix the bug. To test your eval_call() and localize the bug, you may define the variable webpage to hold any webpage text (presumably including JavaScript) that you like. Hint: Pay careful attention to environments. Remember that a function is defined in one environment but called in another. 

(2) Automatic Debugging: A key part of debugging is minimizing test cases to localize defects. We want the smallest test case possible that is still "interesting". For example, suppose we start with a too-big JavaScript test case:

       var x = 1;
       var y = 2;
       var z = 3;
       x = y + z; 
       y = z; 
       z = x + x; 

And further suppose that the bug in question triggers on any addition involving defined variables. In that case, both of these two smaller test cases are also "interesting": 

       var x = 1;
       var y = 2;
       var z = 3;
       x = y + z; 

And:

       var x = 1;
       var z = 3;
       z = x + x; 

We want to find the smallest test case we can that still shows the bug (i.e., is still "interesting"). One way to do this is to manually remove lines and check to see if the result is still interesting. But that is time consuming! Why don't we just write a program to do that for us? We'll represent a test case as a list. For example, our test case above might be: 

      test1 = [ ("var","x"),                  # var x 
                ("var","y"),                  # var y 
                ("var","z"),                  # var z 
                ("add",["x","y","z"]),        # x = y + z
                ("set",["y","z"]),            # y = z 
                ("add",["z","x","x"]), ]      # z = x + x 

To see if a test case is still "interesting", we would run our program on it and look for errors or crashes or whatnot. We'll abstract that by assuming that we have a function call interesting(test) that takes as input a test case and returns true if it is interesting. For example:

      def interesting1(test):
    
            # The test is interesting if it contains "A + B" on some line and "var A" and "var B" _before_ that line. Let's hack 
            something up that simulates that. 
        
             for i in range(len(test)):
            
                     line = test[i] 
                
                     if line[0] == "add":
                    
                            if line[1] == [x for x in line[1] if ("var",x) in test[:i]]:
                                
                                    return True 
             return False 

Your task is to write a function autodebug(test,interesting). It returns a smallest subset (sublist) of test such that that subset is makes interesting returns true. "Smallest" is measured by list length. You may assume that that input test is interesting. Hint: Compose "find all subsets" with "find max". 

(3) Fix The Bug
