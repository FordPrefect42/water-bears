"Dynamic Variables
let cj = "Christopher Adams"
<<<<<<< HEAD
let nVars = {
 \"appname" : "Water Bears", 
 \"author" : name, 
 \"copyright" : "", 
 \"credits" : name . ", " . cj,
 \"license" : "", 
 \"version" : "0.0.1", 
=======
let dVars = {
 \"appname" : "Water Bears", 
 \"author" : name, 
 \"copyright" : "", 
 \"license" : "", 
 \"version" : "0.1.0", 
>>>>>>> stable
 \"maintainers" : name . ", " . cj,
 \"email" : 'msirabel@gmail.com', 
 \"status" : "Prototype", 
 \"module" : ""}

<<<<<<< HEAD
let uVars = copy(nVars)

unlet uVars.credits
unlet uVars.author
"unlet dVars.credits
unlet uVars.maintainers
=======
let nVars = copy(dVars)
let nVars.credits = dVars.maintainers
>>>>>>> stable

"__smail__      =il.com"
"__email__
 "\"credits" : credlist, 

augroup Skeletons
<<<<<<< HEAD
 autocmd BufNewFile,BufRead *.py call g:varLoop(uVars)
=======
 autocmd BufNewFile,BufRead *.py call g:varLoop(dVars)
>>>>>>> stable
 autocmd BufNewFile *.py call g:varLoop(nVars)
augroup END
fun g:varLoop(list)
 try
  for var in keys(a:list)
   call PythonMetaUpdate(var, a:list[var])
  endfor
  catch
 endtry
endfunction
