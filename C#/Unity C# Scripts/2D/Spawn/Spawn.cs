using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawn : MonoBehaviour
{
    public GameObject SpawnPrefab; // This is the prefab you want to spawn .. If you change this name rename the reference at 16:21 aka line 16, character 21
    public float minX;
    public float maxX;
    public float minY;
    public float maxY;


    private void Spawn()
    {
        Instantiate(SpawnPrefab, new Vector2(Random.Range(minX, maxX), Random.Range(minY, maxY)), Quaternion.identity);
    }
    
    void Start()
    {
        InvokeRepeating("Spawn", 1, 1);
    }
}