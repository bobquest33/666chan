'use strict';

angular.module('frontendApp')
    .controller('BoardsController', function($scope, Board) {
        Board.query(function(data) {
            $scope.boards = data.boards;
        });

        $scope.board = new Board();
        $scope.addBoard = function(board) {
            var new_board = angular.copy($scope.board);
            $scope.board.$save(function(u, headers) {
                if (u.status == "okay") {
                    $scope.boards.push(new_board);
                }
            });
        };
    });
