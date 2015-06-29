'use strict';

angular.module('frontendApp')
    .factory('Board', function($resource) {
        return $resource('http://localhost:5000/boards', {}, {'query': {isArray: false}});
    });
