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
