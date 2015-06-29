'use strict';

angular.module('frontendApp')
    .controller('BoardsController', function($scope, Board) {
        Board.query(function(data) {
            $scope.boards = data.boards;
        });
    });
