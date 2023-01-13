-- 코드를 입력하세요
SELECT f.FLAVOR
FROM FIRST_HALF f, ICECREAM_INFO i
WHERE f.flavor = i.flavor and f.total_order > 3000 and i.ingredient_type = 'fruit_based'
ORDER BY f.total_order DESC