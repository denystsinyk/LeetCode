from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # want to loop all the directs and check if the number equals 
        # bfs 
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if original_color == color:
            return image
        
        q = deque([(sr, sc)])
        image[sr][sc] = color
        
        while q:
            r, c = q.popleft()

            # dir check
            for dr, dc in d:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    # append and change color
                    q.append((nr, nc))
                    image[nr][nc] = color
    
        
        return image

        

