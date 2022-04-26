using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Photon.Pun;

public class PlayersInRooms : MonoBehaviour
{
        //Refs
    public TMP_Text playersInRoom;
    private LoadBalancingClient loadBalancingClient;

    void Update()
    {
        playersInRoom.text = ("Players In Room: " + loadBalancingClient.PlayersInRoomsCount);
    }
}