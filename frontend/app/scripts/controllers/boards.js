'use strict';

angular.module('frontendApp')
    .controller('BoardsController', function($scope, Board) {
        Board.query(function(data) {
            $scope.boards = data.boards;
        });

        $scope.error = "";

        $scope.board = new Board();
        $scope.addBoard = function(board) {
            var new_board = angular.copy($scope.board);
            $scope.board.$save(function(u, headers) {
                if (u.status == "okay") {
                    $scope.boards.push(new_board);
                } else if (u.status == "duplicate entry") {
                    $scope.error = "Board already exists!";
                } else if (u.status == "missing args") {
                    $scope.error = "A Board needs at least a Shortname and a Name.";
                }
            });
        };
    });
