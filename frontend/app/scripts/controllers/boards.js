'use strict';

angular.module('frontendApp')
    .controller('BoardsController', function($scope, Board) {
        Board.query(function(data) {
            $scope.boards = data.boards;
        });

        $scope.board = new Board();
        $scope.addBoard = function(board) {
            $scope.board.$save(function() {});
        };
    });
