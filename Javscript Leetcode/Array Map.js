/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var aarray = [];
    for (let i = 0; i < arr.length; i++) {
      aarray.push(fn(arr[i],i));
    }
    return aarray;
  };