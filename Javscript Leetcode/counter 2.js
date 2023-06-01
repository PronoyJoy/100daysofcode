/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
    counterValue = init //value pass
 
    const counter = {
         increment: function() {
             counterValue += 1;
             return counterValue;
         },
         
         reset: function() {
             counterValue = init
             return counterValue;
         },
         
         decrement: function() {
             counterValue -=1
             return counterValue;
         },
      };
 
         return counter;
     }
 
 
 /**
  * const counter = createCounter(5)
  * counter.increment(); // 6
  * counter.reset(); // 5
  * counter.decrement(); // 4
  */