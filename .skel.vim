"Dynamic Variables
let cj = "Christopher Adams"
let dVars = {
 \"appname" : "Water Bears", 
 \"author" : name, 
 \"copyright" : "", 
 \"license" : "", 
 \"version" : "0.1.0", 
 \"maintainers" : name . ", " . cj,
 \"email" : 'msirabel@gmail.com', 
 \"status" : "Prototype", 
 \"module" : ""}

let nVars = copy(dVars)
let nVars.credits = dVars.maintainers

"__smail__      =il.com"
"__email__
 "\"credits" : credlist, 

augroup Skeletons
 autocmd BufNewFile,BufRead *.py call g:varLoop(dVars)
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
