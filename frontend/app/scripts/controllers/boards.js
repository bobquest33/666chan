'use strict';

angular.module('frontendApp')
    .controller('BoardsController', function($scope) {
        $scope.boards = [
            {
                shortname: 'b',
                description: 'Random'
            },
            {
                shortname: 'd',
                description: 'Die in Hell'
            }
        ];
    });
