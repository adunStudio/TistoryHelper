(function() {
    'use strict'

    var Utils ={
        isFunction: function(obj) {
            return Object.prototype.toString.call(obj) === '[object Function]';
        },
        isObject: function(obj) {
            var type = typeof obj;
            return type === 'function' || type === 'object' || !!obj;
        },
        isArray: Array.isArray || function(obj) {
            return Object.prototype.toString.call(obj) === '[object Array]';
        },
        isPlainObject: function(obj) {
            return this.isObject(obj) && !this.isArray(obj) && !this.isFunction(obj);
        },
        extend: function(obj) {
            obj = this.isPlainObject(obj) || this.isArray(obj) ? obj : {};

            var i = 1,
                key

            for(i = 1; i < obj.length; ++i)
            {
                for(key in obj[i])
                {
                    if(obj[i].hasOwnProperty(key))
                    {

                    }
                }
            }
        }
    }
})();