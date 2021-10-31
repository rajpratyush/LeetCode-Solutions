func orangesRotting(grid [][]int) int {
    q := [][2]int{}
    m, n := len(grid), len(grid[0])
    cntFreshes := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 2 {
                q = append(q, [2]int{i, j})
            } else if grid[i][j] == 1 {
                cntFreshes++
            }
        }
    }
    step := 0
    dirs := [][]int{{0, -1}, {0, 1}, {1, 0}, {-1, 0}}
    for len(q) > 0 {
        k := len(q)
        for i := 0; i < k; i++ {
            cur := q[0]
            q = q[1:]
            for _, d := range dirs {
                x, y := cur[0] + d[0], cur[1] + d[1]
                if x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1 {
                    grid[x][y] = 2
                    cntFreshes--
                    q = append(q, [2]int{x, y})
                }
            }
        }
        if len(q) > 0 {
            step++
        }
    }
    if cntFreshes == 0 {
        return step
    }
    return -1
}