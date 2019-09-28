import ply.lex as lex
import ply.yacc as yacc
import graphics as graphics
import jstokens
import jsgrammar
import jsinterp 
import htmltokens
import htmlgrammar
import htmlinterp

htmllexer  = lex.lex(module=htmltokens) 
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml") 
jslexer    = lex.lex(module=jstokens) 
jsparser   = yacc.yacc(module=jsgrammar,tabmodule="parsetabjs") 
env_lookup = jsinterp.env_lookup
eval_exp = jsinterp.eval_exp
JSReturn = jsinterp.JSReturn
eval_stmts = jsinterp.eval_stmts
env_update = jsinterp.env_update



def eval_call(exp,env): 
    
    # Recall: exp = (fname, args, body, fenv) 
    
    fname = exp[1]
    args = exp[2] 
    fvalue = env_lookup(fname,env) 
    
    if fname == "write":
        
        argval = eval_exp(args[0],env)
        
        output_sofar = env_lookup("javascript output",env)
        
        env_update("javascript output",output_sofar + str(argval),env)
        
    elif fvalue[0] == "function":
        
        fparams = fvalue[1] 
        
        fbody = fvalue[2] 
        
        fenv = fvalue[3]
        
        if len(fparams) != len(args):
            
            print ("ERROR: wrong number arguments to " + fname)
            
        else: 
            
            # make a new environment frame
            newenv = (fenv,{ }) 
            
            for i in range(len(args)):
                
                argval = eval_exp(args[i],env)
                
                (newenv[1])[fparams[i]] = argval
                
            # evaluate the body in the new frame
            try:
                eval_stmts(fbody,newenv)
                
                return None
                
            except JSReturn as r:
                
                return r.retval
    else:
        
        print ("ERROR: call to non-function " + fname)

jsinterp.eval_call = eval_call

webpage = """<html>
<p>
The correct answer is 3.0 4.0: 
<script type="text/javascript">
function tvtropes(tgwtg) {
    var theonion = "reddit" + "pennyarcade";
    var loadingreadyrun = function(extracredits) {
        write(tgwtg);
        write(" "); 
        write(extracredits);
    } ;    
    return loadingreadyrun; 
}
var yudkowsky = tvtropes(3); 
var tgwtg = 888;
var extracredits = 999;
yudkowsky(4); 
/* Shoutouts to a random sampling of Western Web Comedy,
 * Analysis and Literature circa 2012. Bonus points if you
 * can get any of them to return the favor. Udacity needs 
 * a tvtropes page. :-) */ 
</script>
</p> 
<hr> </hr> 
<img src="cs262.png"> </img> 
</html>
"""


htmlast = htmlparser.parse(webpage,lexer=htmllexer) 
graphics.initialize() # let's start rendering a webpage
htmlinterp.interpret(htmlast) 
graphics.finalize() # we're done rendering this webpage
